from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from django.db import transaction

from University_Faculty.accounts.models import Student, Teacher
from University_Faculty.common.helpers import BootstrapFormMixin

UserModel = get_user_model()


class CreateStudentForm(BootstrapFormMixin, auth_forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    first_name = forms.CharField(
        max_length=Student.FIRST_NAME_MAX_LENGTH
    )

    last_name = forms.CharField(
        max_length=Student.LAST_NAME_MAX_LENGTH
    )

    email = forms.EmailField()

    profile_picture = forms.FileField()

    date_of_birth = forms.DateTimeField()

    gender = forms.ChoiceField(
        choices=Student.GENDERS
    )

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=commit)
        user.is_student = True
        user.save()

        student_profile = Student(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            profile_picture=self.cleaned_data['profile_picture'],
            date_of_birth=self.cleaned_data['date_of_birth'],
            gender=self.cleaned_data['gender'],
            user=user,
        )

        if commit:
            student_profile.save()

        return user

    class Meta:
        model = UserModel
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name', 'profile_picture')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Enter your first name',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Enter your last name',
            }),
            'picture': forms.TextInput(attrs={
                'placeholder': 'Enter your image url',
            }),
        }


class CreateTeacherForm(BootstrapFormMixin, auth_forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    first_name = forms.CharField(
        max_length=Student.FIRST_NAME_MAX_LENGTH
    )

    last_name = forms.CharField(
        max_length=Student.LAST_NAME_MAX_LENGTH
    )

    email = forms.EmailField()

    profile_picture = forms.FileField()

    date_of_birth = forms.DateTimeField()

    gender = forms.ChoiceField(
        choices=Student.GENDERS
    )

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=commit)
        user.is_teacher = True
        user.save()
        teacher_profile = Teacher(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            profile_picture=self.cleaned_data['profile_picture'],
            date_of_birth=self.cleaned_data['date_of_birth'],
            gender=self.cleaned_data['gender'],
            user=user
        )

        if commit:
            teacher_profile.save()

        return user

    class Meta:
        model = UserModel
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name', 'profile_picture')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Enter your first name',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Enter your last name',
            }),
            'picture': forms.TextInput(attrs={
                'placeholder': 'Enter your image url',
            }),
        }

