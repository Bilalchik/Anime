# Generated by Django 4.1.1 on 2022-09-20 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_episode_season_alter_season_anime'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='slug',
            field=models.SlugField(default=1, editable=False),
            preserve_default=False,
        ),
    ]
