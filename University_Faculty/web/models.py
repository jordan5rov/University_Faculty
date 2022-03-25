from django.db import models


class News(models.Model):
    TITLE_MAX_LENGTH = 30
    title = models.CharField(
        max_length=TITLE_MAX_LENGTH
    )
    image = models.FileField(
        upload_to='news/',
        blank=True
    )
    description = models.TextField()


class Event(models.Model):
    TITLE_MAX_LENGTH = 30
    title = models.CharField(
        max_length=TITLE_MAX_LENGTH
    )
    image = models.FileField(
        upload_to='events/',
        blank=True
    )
    description = models.TextField()
    date = models.DateTimeField()
