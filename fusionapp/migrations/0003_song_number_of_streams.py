# Generated by Django 2.1.7 on 2019-12-21 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fusionapp', '0002_album_artist_platform_playlist_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='number_of_streams',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]