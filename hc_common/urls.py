#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from hc_common import views

app_name = "hc_common"
urlpatterns = [
    url(r'^documento/$', views.DocumentoList.as_view(), name='Documento-list'),
    url(r'^documento/(?P<pk>[0-9]+)/$', views.DocumentoDetails.as_view(),name='Documento-detail'),
    url(r'^persona/$', views.PersonaList.as_view(), name='Persona-list'),
    url(r'^persona/(?P<pk>[0-9]+)/$', views.PersonaDetails.as_view(),name='Persona-detail'),
]