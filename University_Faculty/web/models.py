import datetime

from django.core.exceptions import ValidationError
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
    description = models.TextField()
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
    description = models.TextField()
    date = models.DateTimeField(default=datetime.datetime.now)
    published_on = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):
        if self.date.date() < datetime.date.today():
            raise ValidationError("The date cannot be in the past!")
        super(Event, self).save(*args, **kwargs)
