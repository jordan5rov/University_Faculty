from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from University_Faculty.accounts.models import Student, Teacher
from University_Faculty.common.helpers import BootstrapFormMixin

UserModel = get_user_model()


class CreateStudentForm(BootstrapFormMixin, auth_forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.user = user
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

    def save(self, commit=True):
        user = super().save(commit=commit)

        student_profile = Student(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            profile_picture=self.cleaned_data['profile_picture'],
            date_of_birth=self.cleaned_data['date_of_birth'],
            gender=self.cleaned_data['gender'],
            user=user
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
    first_name = forms.CharField(
        max_length=Teacher.FIRST_NAME_MAX_LENGTH
    )

    last_name = forms.CharField(
        max_length=Teacher.LAST_NAME_MAX_LENGTH
    )

    email = forms.EmailField()

    profile_picture = forms.URLField()

    date_of_birth = forms.DateTimeField()

    gender = forms.ChoiceField(
        choices=Teacher.GENDERS
    )

    def save(self, commit=True):
        user = super().save(commit=commit)

        student_profile = Teacher(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
            profile_picture=self.cleaned_data['profile_picture'],
            date_of_birth=self.cleaned_data['date_of_birth'],
            gender=self.cleaned_data['gender'],
            user=user
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


class DeleteStudentForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Student
        fields = ()
