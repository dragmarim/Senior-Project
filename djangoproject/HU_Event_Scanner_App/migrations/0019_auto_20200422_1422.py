# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2020-04-22 14:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HU_Event_Scanner_App', '0018_scan_new_scan'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='scan',
            unique_together=set([('student_id', 'chapel_envt_no')]),
        ),
    ]
