#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django_cron import CronJobBase, Schedule
from django.contrib.auth.models import User
from HU_Event_Scanner_App.models import Scan
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.forms.models import model_to_dict
import json
from django.core.serializers.json import DjangoJSONEncoder

class MyCronJob(CronJobBase):
	RUN_EVERY_MINS = 2

	schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
	code = 'HU_Event_Scanner_App.views.MyCronJob'

	def do(self):
		users = User.objects.filter(groups__name='v');
		for user in users:
			user.is_active = True
			user.save()

# Create your views here.
def index(request):
    return render(request, '/opt/djangoproject/HU_Event_Scanner_App/templates/HU_Event_Scanner_App/index.html')

@login_required
def moderator(request):
	#notify_user(1, repeat=20, repeat_until=None)
	return render(request, '/opt/djangoproject/HU_Event_Scanner_App/templates/HU_Event_Scanner_App/moderator.html')

@login_required
def logout_request(request):
	logout(request)
	return redirect('/')

@csrf_exempt
def save_scan(request):
	if request.method == 'POST':
		#stid = Scan.objects.get()
		#stid.student_id = request.POST['scan']
		stid = Scan(student_id = request.POST.get('scan',0),chapel_envt_no = request.POST.get('envt_no',0))
		stid.save()
		message = 'update successful'
	return HttpResponse(message)

def testTim(request):
        return render(request, '/opt/djangoproject/HU_Event_Scanner_App/templates/HU_Event_Scanner_App/testTim.html')

def testLandon(request):
	return render(request, '/opt/djangoproject/HU_Event_Scanner_App/templates/HU_Event_Scanner_App/testLandon.html')

def scanOutput(request):
	#return JsonResponse(serializers.serialize('json', Scan.objects.filter(new_scan=True).values()), safe=False)
	data = Scan.objects.filter(new_scan=True).values('student_id','date','chapel_envt_no')
	list_result = [entry for entry in data]
	scans = json.dumps(list_result,indent=4,cls=DjangoJSONEncoder)
	return HttpResponse(scans, content_type='application/json')

@login_required
def testLucas(request):
        return render(request, '/opt/djangoproject/HU_Event_Scanner_App/templates/HU_Event_Scanner_App/testLucas.html')

#context={"events": Event.objects.all}
