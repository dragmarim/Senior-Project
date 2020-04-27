"""HU_Event_Scanner URL Configuration

iThe `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from HU_Event_Scanner_App import views
from HU_Event_Scanner_App.views import save_scan
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "HU_Event_Scanner_App"

urlpatterns = [
   url(r"^$", views.moderator, name="moderator"),
   url(r"^testTim/$", views.testTim, name="testTim"),
   url(r"^testLandon/$", views.testLandon, name="testLandon"),
   url(r"^testLucas/$", views.testLucas, name="testLucas"),
   url(r"^scanOutput/$", views.scanOutput, name="scanOutput"),
   url(r'login/$', auth_views.login, name='login'),
   url(r'^save_scan/', save_scan),
   #url(r'^logout/$', auth_views.logout, name='logout'),
   url(r'^logout/$', views.logout_request, name='logout'),
]
