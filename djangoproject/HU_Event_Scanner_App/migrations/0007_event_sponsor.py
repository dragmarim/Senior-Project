# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-28 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HU_Event_Scanner_App', '0006_remove_event_sponsor'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='sponsor',
            field=models.CharField(default='N/A', max_length=255),
        ),
    ]
