# Generated by Django 3.0.5 on 2020-05-23 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_auto_20200523_1916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friend',
            old_name='occ',
            new_name='occupation',
        ),
        migrations.RenameField(
            model_name='friend',
            old_name='ph',
            new_name='phone',
        ),
    ]