from django.db import models


class News(models.Model):
    TITLE_MAX_LENGTH = 30
    IMAGE_UPLOAD_TO_DIRECTORY = 'news/'
    title = models.CharField(
        max_length=TITLE_MAX_LENGTH
    )
    image = models.FileField(
        upload_to=IMAGE_UPLOAD_TO_DIRECTORY,
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
        blank=True
    )
    description = models.TextField()
    date = models.DateTimeField()
    published_on = models.DateTimeField(
        auto_now=True
    )
