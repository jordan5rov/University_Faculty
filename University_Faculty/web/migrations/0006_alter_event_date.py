# Generated by Django 4.0.3 on 2022-04-25 14:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_remove_event_organizer_remove_event_participants_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.date(2022, 4, 25)),
        ),
    ]
