from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from University_Faculty.classroom.models import Subject, Student, Teacher, Question, Quiz
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
        user = super().save(commit=commit)
        user.type = STUDENT

        student = Student.objects.create(user=user)
        student.interests.add(*self.cleaned_data.get('interests'))

        if commit:
            student.save()

        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2')


class TeacherCreateForm(BootstrapFormMixin, auth_forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

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


class StudentInterestForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('interests',)
        widgets = {
            'interests': forms.CheckboxSelectMultiple
        }


class TeacherEditQuizForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Quiz
        fields = ('name', 'subject', 'max_score', 'required_score_to_pass', 'time')


class QuizForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Quiz
        fields = ('name', 'subject', 'max_score', 'required_score_to_pass', 'time')


class SubjectForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Subject
        fields = ('name', 'color')


class QuestionForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Question
        fields = ('question', 'option_1', 'option_2', 'option_3', 'option_4', 'correct_option')
