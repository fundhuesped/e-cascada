#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from hc_notificaciones import views

app_name = "hc_notificaciones"
urlpatterns = [
    url(r'^createNotifications/$', views.CreateNotifications.as_view(), name='Create-Notifications'),
]
