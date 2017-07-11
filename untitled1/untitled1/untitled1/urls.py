"""untitled1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
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
from Studierendenverwaltung.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^lehveranstaltung/$', lehveranstaltung_list, name= 'lehveranstaltungen'),
    url(r'^lehveranstaltung/neue/$', lehveranstaltung_new, name= 'addlehveranstaltung'),
    url(r'^lehveranstaltung/edit/(?P<pk>[0-9]+)/$', lehveranstaltung_edit, name='editlehveranstaltung'),
    url(r'^lehveranstaltung/delete/(?P<pk>[0-9]+)/$', lehveranstaltung_delete, name='deletelehveranstaltung'),

    # studierende
    url(r'^studierende/$', studierenden_list, name= 'Studierenden'),
    url(r'^studierende/neueStudent/$', studierenden_new, name= 'addStudent'),
    url(r'^studierende/edit/(?P<pk>[0-9]+)/$', studierenden_edit, name='editStudent'),
    url(r'^studierende/delete/(?P<pk>[0-9]+)/$', studierenden_delete, name='deleteStudent'),

    url(r'^studierende/Einschreibung/(?P<pk>[0-9]+)/$', studierenden_enschreiben, name='einschreibung'),
    #url(r'^studierende/Einschreibung/(?P<pk>[0-9]+)/$', studierenden_enschreiben, name='einschreibung'),
]
