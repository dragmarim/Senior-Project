# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now

def get_deadline():
	return datetime.now();

class Event(models.Model):
	name = models.CharField(max_length=255)
	event_id = models.IntegerField(default=0)
	start_date = models.DateTimeField(default=now)
	sponsor = models.CharField(max_length=255,default='N/A')
	end_date = models.DateTimeField(default=now)
	core = models.BooleanField(default=False)
	def __str__(self):
		return self.name

class Scan(models.Model):
	def __str__(self):
		return str(self.student_id)
	student_id = models.IntegerField()
	time_scanned = models.DateTimeField(default=now)
