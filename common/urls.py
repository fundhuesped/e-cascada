from django.conf.urls import url
from common import views

app_name = "common"
urlpatterns = [
    url(r'^coding/$', views.CodingList.as_view(), name='coding-list'),
    url(r'^coding/(?P<pk>[0-9]+)/$', views.CodingDetail.as_view(),name='coding-detail'),
    url(r'^identifier/$', views.IdentifierList.as_view(), name='Identifier-list'),
    url(r'^identifier/(?P<pk>[0-9]+)/$', views.IdentifierDetail.as_view(),name='Identifier-detail'),
    url(r'^identifier-type/$', views.IdentifierTypeList.as_view(), name='IdentifierType-list'),
    url(r'^identifier-type/(?P<pk>[0-9]+)/$', views.IdentifierTypeDetail.as_view(),name='IdentifierType-detail'),
    url(r'^identifier-period/$', views.IdentifierPeriodList.as_view(), name='IdentifierPeriod-list'),
    url(r'^identifier-period/(?P<pk>[0-9]+)/$', views.IdentifierPeriodDetail.as_view(),name='IdentifierPeriod-detail'),
    url(r'^address/$', views.AddressList.as_view(), name='Address-list'),
    url(r'^address/(?P<pk>[0-9]+)/$', views.AddressDetail.as_view(), name='Address-detail'),
    url(r'^address-point-period/$', views.AddressPointPeriodList.as_view(), name='AddressPointPeriod-list'),
    url(r'^address-point-period/(?P<pk>[0-9]+)/$', views.AddressPointPeriodDetail.as_view(),name='AddressPointPeriod-detail'),
    url(r'^address-line/$', views.AddressLineList.as_view(), name='AddressLine-list'),
    url(r'^address-line/(?P<pk>[0-9]+)/$', views.AddressLineDetail.as_view(),name='AddressLine-detail'),
    url(r'^contact-point/$', views.ContactPointList.as_view(), name='ContactPoint-list'),
    url(r'^contact-point/(?P<pk>[0-9]+)/$', views.ContactPointDetails.as_view(),name="ContactPoint-detail"),
    url(r'^contact-point-period/$', views.ContactPointPeriodList.as_view(),name="ContactPointPeriod-list"),
    url(r'^contact-point-period/(?P<pk>[0-9]+)/$', views.ContactPointPeriodDetail.as_view(),name='ContactPointPeriod-detail'),
    url(r'^name-period/$', views.NamePeriodList.as_view(), name='NamePeriod-list'),
    url(r'^name-period/(?P<pk>[0-9]+)/$', views.NamePeriodDetail.as_view(),name='NamePeriod-detail'),
    url(r'^human-name/$', views.HumanNameList.as_view(),name="HumanName-list"),
    url(r'^human-name/(?P<pk>[0-9]+)/$', views.HumanNameDetails.as_view(),name='HumanName-detail'),
    url(r'^organization-contact/$', views.OrganizationContactList.as_view(),name="OrganizationContact-list"),
    url(r'^organization-contact/(?P<pk>[0-9]+)/$', views.OrganizationContactDetails.as_view(),name='OrganizationContact-detail'),
    url(r'^organization/$', views.OrganizationList.as_view(),name="Organization-list"),
    url(r'^organization/(?P<pk>[0-9]+)/$', views.OrganizationDetails.as_view(),name='Organization-detail'),
    url(r'^day-of-week/$', views.DayOfWeekList.as_view(),name="DayOfWeek-list"),
    url(r'^day-of-week/(?P<pk>[0-9]+)/$', views.DayOfWeekDetails.as_view(),name='DayOfWeek-detail'),
]