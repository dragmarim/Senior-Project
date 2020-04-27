# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from HU_Event_Scanner_App.models import Scan

from django.contrib import admin

class ScanAdmin(admin.ModelAdmin):
	list_display = ('student_id', 'date', 'chapel_envt_no', 'new_scan')

admin.site.register(Scan, ScanAdmin)
