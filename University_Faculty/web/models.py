from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

from University_Faculty.classroom.models import UniversityUser, Teacher
from University_Faculty.common.constants import *


class News(models.Model):
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
    title = models.CharField(
        max_length=TITLE_MAX_LENGTH
    )
    image = models.FileField(
        upload_to=EVENT_IMAGE_UPLOAD_TO_DIRECTORY,
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
