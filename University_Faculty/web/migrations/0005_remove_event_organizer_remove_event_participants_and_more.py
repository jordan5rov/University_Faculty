# Generated by Django 4.0.3 on 2022-04-25 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_event_organizer_alter_news_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='organizer',
        ),
        migrations.RemoveField(
            model_name='event',
            name='participants',
        ),
        migrations.RemoveField(
            model_name='news',
            name='author',
        ),
    ]
