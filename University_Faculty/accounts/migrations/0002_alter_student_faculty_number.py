# Generated by Django 4.0.3 on 2022-03-31 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='faculty_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
