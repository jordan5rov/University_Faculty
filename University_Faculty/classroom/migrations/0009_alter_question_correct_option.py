# Generated by Django 4.0.3 on 2022-04-23 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0008_remove_quiz_is_taken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correct_option',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0),
        ),
    ]
