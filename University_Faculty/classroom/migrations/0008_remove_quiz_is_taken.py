# Generated by Django 4.0.3 on 2022-04-23 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0007_quiz_is_taken'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='is_taken',
        ),
    ]