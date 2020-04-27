# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now

def get_deadline():
	return datetime.now();

class Scan(models.Model):
	student_id = models.IntegerField()
	#add_date = models.DateField()
	date = models.DateTimeField(auto_now_add=True)
	chapel_envt_no = models.IntegerField()
	new_scan = models.BooleanField(default=True)

	class Meta:
		unique_together = ('student_id', 'chapel_envt_no',)
