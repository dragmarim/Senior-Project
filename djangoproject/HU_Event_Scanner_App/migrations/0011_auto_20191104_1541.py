# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-04 15:41
from __future__ import unicode_literals

import HU_Event_Scanner_App.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HU_Event_Scanner_App', '0010_auto_20191104_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(default=HU_Event_Scanner_App.models.get_deadline, editable=False),
        ),
    ]
