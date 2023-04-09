# Generated by Django 3.2.18 on 2023-04-09 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='discord',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='playstation',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='steam',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitch',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='xbox',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='youtube',
            field=models.URLField(blank=True),
        ),
    ]