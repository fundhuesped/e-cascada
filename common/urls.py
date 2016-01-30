from django.conf.urls import url
from common import views

urlpatterns = [
    url(r'^coding/$', views.CodingList.as_view(), name='coding-list'),
    url(r'^coding/(?P<pk>[0-9]+)/$', views.CodingDetail.as_view(),name='coding-detail'),
    url(r'^identifier-type/$', views.IdentifierTypeList.as_view(), name='IdentifierType-list'),
    url(r'^identifier-type/(?P<pk>[0-9]+)/$', views.IdentifierTypeDetail.as_view(),name='IdentifierType-detail'),
    url(r'^identifier-period/$', views.IdentifierPeriodList.as_view(), name='IdentifierPeriod-list'),
    url(r'^identifier-period/(?P<pk>[0-9]+)/$', views.IdentifierPeriodDetail.as_view(),name='IdentifierPeriod-detail'),
    url(r'^contact-point-period/$', views.ContactPointPeriodList.as_view(), name='ContactPointPeriod-list'),
    url(r'^contact-point-period/(?P<pk>[0-9]+)/$', views.ContactPointPeriodDetail.as_view(),name='ContactPointPeriod-detail'),
    url(r'^address-point-period/$', views.AddressPointPeriodList.as_view(), name='AddressPointPeriod-list'),
    url(r'^address-point-period/(?P<pk>[0-9]+)/$', views.AddressPointPeriodDetail.as_view(),name='AddressPointPeriod-detail'),
    url(r'^name-period/$', views.AddressPointPeriodList.as_view(), name='NamePeriod-list'),
    url(r'^name-period/(?P<pk>[0-9]+)/$', views.AddressPointPeriodDetail.as_view(),name='NamePeriod-detail'),
    url(r'^address-line/$', views.AddressLineList.as_view(), name='AddressLine-list'),
    url(r'^address-line/(?P<pk>[0-9]+)/$', views.AddressLineDetail.as_view(),name='AddressLine-detail'),
]