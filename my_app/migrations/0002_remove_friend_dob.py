# Generated by Django 3.0.5 on 2020-05-22 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='dob',
        ),
    ]