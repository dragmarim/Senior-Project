# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-09 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HU_Event_Scanner_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('student_id', models.IntegerField()),
                ('time_scanned', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='core',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='end_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='event',
            name='start_date',
            field=models.DateField(auto_now=True),
        ),
    ]
