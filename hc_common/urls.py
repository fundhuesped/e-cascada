#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from hc_common import views

app_name = "hc_common"
urlpatterns = [
    url(r'^sexType/$', views.SexTypeList.as_view(), name='SexType-list'),
    url(r'^sexType/(?P<pk>[0-9]+)/$', views.SexTypeDetails.as_view(),name='SexType-detail'),
    url(r'^documentType/$', views.DocumentTypeList.as_view(), name='DocumentType-list'),
    url(r'^documentType/(?P<pk>[0-9]+)/$', views.DocumentTypeDetails.as_view(),name='DocumentType-detail'),
    url(r'^persona/$', views.PersonaList.as_view(), name='Persona-list'),
    url(r'^persona/(?P<pk>[0-9]+)/$', views.PersonaDetails.as_view(),name='Persona-detail'),
]