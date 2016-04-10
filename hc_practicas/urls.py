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

    url(r'^dayOfWeek/$', views.DayOfWeekList.as_view(), name='DayOfWeek-list'),
    url(r'^dayOfWeek/(?P<pk>[0-9]+)/$', views.DayOfWeekDetails.as_view(), name='DayOfWeek-detail'),

    url(r'^agenda/$', views.AgendaList.as_view(), name='Agenda-list'),
    url(r'^agenda/(?P<pk>[0-9]+)/$', views.AgendaDetails.as_view(), name='Agenda-detail'),

    url(r'^period/$', views.PeriodList.as_view(), name='Period-list'),
    url(r'^period/(?P<pk>[0-9]+)/$', views.PeriodDetails.as_view(), name='Period-detail'),

    url(r'^turno/$', views.TurnoList.as_view(), name='Turno-list'),
    url(r'^turno/(?P<pk>[0-9]+)/$', views.TurnoDetails.as_view(), name='Turno-detail'),
]
