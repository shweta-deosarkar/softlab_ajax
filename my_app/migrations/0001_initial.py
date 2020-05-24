# Generated by Django 3.0.5 on 2020-05-19 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(max_length=100, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('likes', models.CharField(max_length=250)),
                ('dob', models.DateField()),
                ('lives_in', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
    ]
