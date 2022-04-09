from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from django.db import transaction

from University_Faculty.classroom.models import Subject, Student
from University_Faculty.common.helpers import BootstrapFormMixin


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

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
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

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2')
