import datetime

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

from University_Faculty.classroom.models import UniversityUser, Teacher


class News(models.Model):
    TITLE_MAX_LENGTH = 30
    IMAGE_UPLOAD_TO_DIRECTORY = 'news/'
    title = models.CharField(
        max_length=TITLE_MAX_LENGTH
    )
    image = models.FileField(
        upload_to=IMAGE_UPLOAD_TO_DIRECTORY,
        null=True,
        blank=True
    )
    description = models.TextField(
        validators=(
            MinLengthValidator(30),
            MaxLengthValidator(500),
        )
    )
    published_on = models.DateTimeField(
        auto_now=True
    )


class Event(models.Model):
    TITLE_MAX_LENGTH = 30
    IMAGE_UPLOAD_TO_DIRECTORY = 'events/'
    title = models.CharField(
        max_length=TITLE_MAX_LENGTH
    )
    image = models.FileField(
        upload_to=IMAGE_UPLOAD_TO_DIRECTORY,
        null=True,
        blank=True
    )
    description = models.TextField(
        validators=(
            MinLengthValidator(30),
            MaxLengthValidator(500),
        )
    )
    date = models.DateTimeField()
    published_on = models.DateTimeField(
        auto_now=True
    )
