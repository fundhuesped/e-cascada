#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from hc_common import views

app_name = "hc_common"
urlpatterns = [
    url(r'^sexType/$', views.SexTypeList.as_view(), name='SexType-list'),
    url(r'^sexType/(?P<pk>[0-9]+)/$', views.SexTypeDetails.as_view(), name='SexType-detail'),

    url(r'^documentType/$', views.DocumentTypeList.as_view(), name='DocumentType-list'),
    url(r'^documentType/(?P<pk>[0-9]+)/$', views.DocumentTypeDetails.as_view(), name='DocumentType-detail'),

    url(r'^province/$', views.ProvinceList.as_view(), name='Province-list'),
    url(r'^province/(?P<pk>[0-9]+)/$', views.ProvinceDetails.as_view(), name='Province-detail'),

    url(r'^district/$', views.DistrictList.as_view(), name='District-list'),
    url(r'^district/(?P<pk>[0-9]+)/$', views.DistrictDetails.as_view(), name='District-detail'),

    url(r'^location/$', views.LocationList.as_view(), name='Location-list'),
    url(r'^location/(?P<pk>[0-9]+)/$', views.LocationDetails.as_view(), name='Location-detail'),
]
