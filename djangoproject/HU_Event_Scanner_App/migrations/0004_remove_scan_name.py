# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-09 14:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HU_Event_Scanner_App', '0003_auto_20191009_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scan',
            name='name',
        ),
    ]
