# Generated by Django 4.1.1 on 2022-09-22 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_episode_number_season_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episode',
            name='number',
        ),
    ]
