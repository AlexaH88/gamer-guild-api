# Generated by Django 3.2.18 on 2023-04-21 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='content',
            field=models.CharField(choices=[('Y', 'Yes'), ('M', 'Maybe'), ('N', 'No')], max_length=255),
        ),
    ]
