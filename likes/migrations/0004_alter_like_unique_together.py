# Generated by Django 3.2.18 on 2023-04-07 16:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('likes', '0003_like_event'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('owner', 'event')},
        ),
    ]
