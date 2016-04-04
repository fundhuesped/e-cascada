#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from hc_practicas import views

app_name = "hc_practicas"
urlpatterns = [
    url(r'^especialidad/$', views.EspecialidadList.as_view(), name='Especialidad-list'),
    url(r'^especialidad/(?P<pk>[0-9]+)/$', views.EspecialidadDetails.as_view(), name='Especialidad-detail'),

    url(r'^prestacion/$', views.PrestacionList.as_view(), name='Prestacion-list'),
    url(r'^prestacion/(?P<pk>[0-9]+)/$', views.PrestacionDetails.as_view(), name='Prestacion-detail'),

    url(r'^profesional/$', views.ProfesionalList.as_view(), name='Profesional-list'),
    url(r'^profesional/(?P<pk>[0-9]+)/$', views.ProfesionalDetails.as_view(), name='Profesional-detail'),
]
