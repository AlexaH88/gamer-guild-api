# Generated by Django 3.2.18 on 2023-04-18 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='discord',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='playstation',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='steam',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='twitch',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='xbox',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='youtube',
        ),
    ]