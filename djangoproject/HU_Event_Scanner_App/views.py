#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Event
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, '/opt/djangoproject/HU_Event_Scanner_App/templates/HU_Event_Scanner_App/index.html')

@login_required
def moderator(request):
	return render(request, '/opt/djangoproject/HU_Event_Scanner_App/templates/HU_Event_Scanner_App/moderator.html',context={"events": Event.objects.all})

def testTim(request):
        return render(request, '/opt/djangoproject/HU_Event_Scanner_App/templates/HU_Event_Scanner_App/testTim.html',context={"events": Event.objects.all})

def testLandon(request):
        return render(request, '/opt/djangoproject/HU_Event_Scanner_App/templates/HU_Event_Scanner_App/testLandon.html',context={"events": Event.objects.all})

@login_required
def testLucas(request):
        return render(request, '/opt/djangoproject/HU_Event_Scanner_App/templates/HU_Event_Scanner_App/testLucas.html',context={"events": Event.objects.all})
