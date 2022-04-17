from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from django.core.exceptions import ValidationError
from django.db import transaction

from University_Faculty.classroom.models import Subject, Student, Teacher, Question
from University_Faculty.common.helpers import BootstrapFormMixin
from University_Faculty.common.constants import STUDENT, TEACHER


class StudentCreateForm(BootstrapFormMixin, auth_forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.fields['interests'].widget.attrs['class'] = 'radio-inline'

    interests = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.type = STUDENT

        if commit:
            user.save()

        student = Student.objects.create(user=user)
        student.interests.add(*self.cleaned_data.get('interests'))

        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2')


class TeacherCreateForm(BootstrapFormMixin, auth_forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.fields['specialization'].widget.attrs['class'] = 'checkbox-inline'

    specialization = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.type = TEACHER
        if commit:
            user.save()

        teacher = Teacher.objects.create(user=user)
        teacher.specialization.add(*self.cleaned_data.get('specialization'))

        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2')


class StudentEditForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Student
        fields = ('interests',)


class TeacherEditForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Teacher
        fields = ('specialization',)


class StudentDeleteForm(forms.ModelForm):
    def save(self, commit=True):
        interests = self.instance.subjects_set.all()
        interests.delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Student
        fields = ()


class TeacherDeleteForm(forms.ModelForm):
    def save(self, commit=True):
        specializations = self.instance.subjects_set.all()
        specializations.delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Teacher
        fields = ()


class QuestionForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Question
        fields = ('question', 'option_1', 'option_2', 'option_3', 'option_4', 'correct_option')


class BaseAnswerInlineFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()

        has_one_correct_answer = False
        for form in self.forms:
            if not form.cleaned_data.get('DELETE', False):
                if form.cleaned_data.get('is_correct', False):
                    has_one_correct_answer = True
                    break
        if not has_one_correct_answer:
            raise ValidationError('Mark at least one answer as correct.', code='no_correct_answer')
