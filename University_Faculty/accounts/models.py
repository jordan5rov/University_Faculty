from django.contrib.auth import models as auth_models
from django.core.validators import MinLengthValidator
from django.db import models

from University_Faculty.accounts.managers import UniversityUserManager
from University_Faculty.common.validators import validate_only_letters


class UniversityUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'email'

    objects = UniversityUserManager()


class Student(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    FIRST_NAME_MIN_LENGTH = 3

    LAST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 5

    FACULTY_NUMBER_MAX_LENGTH = 10

    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'
    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]

    PROFILE_PICTURE_UPLOAD_TO_DIRECTORY = 'student/'

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    gender = models.CharField(
        choices=GENDERS,
        max_length=max(len(x) for x, _ in GENDERS),
        default=DO_NOT_SHOW,
        null=True,
        blank=True,
    )

    profile_picture = models.FileField(
        upload_to=PROFILE_PICTURE_UPLOAD_TO_DIRECTORY,
        # default='static/images/student.webp',
    )

    faculty_number = models.IntegerField(
        null=True,
        blank=True
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    user = models.OneToOneField(
        UniversityUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.faculty_number}'


class Teacher(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    FIRST_NAME_MIN_LENGTH = 3

    LAST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 5

    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'
    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]

    PROFILE_PICTURE_UPLOAD_TO_DIRECTORY = 'teacher/'

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    gender = models.CharField(
        choices=GENDERS,
        max_length=max(len(x) for x, _ in GENDERS),
        default=DO_NOT_SHOW,
        null=True,
        blank=True,
    )

    profile_picture = models.FileField(
        upload_to=PROFILE_PICTURE_UPLOAD_TO_DIRECTORY,
        # default='static/images/student.webp',
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    user = models.OneToOneField(
        UniversityUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
