#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from huesped_gateway import views

app_name = "huesped_gateway"
urlpatterns = [
    url(r'^especialidad/$', views.EspecialidadList.as_view(), name='Especialidad-list'),
    url(r'^especialidad/(?P<pk>[0-9]+)/$', views.EspecialidadDetails.as_view(),name='Especialidad-detail'),
]