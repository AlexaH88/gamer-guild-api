# Generated by Django 3.2.18 on 2023-04-14 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, default='../default_event_dseibs', upload_to='images/'),
        ),
    ]
