# Generated by Django 4.0.3 on 2022-04-22 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0006_alter_result_quiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='is_taken',
            field=models.BooleanField(default=False, help_text='Whether the quiz is taken or not'),
        ),
    ]
