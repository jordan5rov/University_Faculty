# Generated by Django 4.0.3 on 2022-04-21 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_alter_teacher_specialization'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='max_score',
            field=models.IntegerField(default=100, help_text='Maximum score for the quiz'),
        ),
    ]