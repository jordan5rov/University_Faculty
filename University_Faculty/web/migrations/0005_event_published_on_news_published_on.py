# Generated by Django 4.0.3 on 2022-03-26 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_event_image_alter_news_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='published_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='news',
            name='published_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
