# Generated by Django 3.1.5 on 2021-01-22 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lnkzio', '0002_shortenedurl_short_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shortenedurl',
            name='short_url',
        ),
    ]
