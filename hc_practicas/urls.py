#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from hc_practicas import views

app_name = "hc_practicas"
urlpatterns = [
    url(r'^especialidad/$', views.EspecialidadList.as_view(), name='Especialidad-list'),
    url(r'^especialidad/(?P<pk>[0-9]+)/$', views.EspecialidadDetails.as_view(),name='Especialidad-detail'),
]