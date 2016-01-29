from django.conf.urls import url
from common import views

urlpatterns = [
    url(r'^coding/$', views.CodingList.as_view(), name='coding-list'),
    url(r'^coding/(?P<pk>[0-9]+)/$', views.CodingDetail.as_view(),name='coding-detail'),
    url(r'^identifierType/$', views.IdentifierTypeList.as_view(), name='IdentifierType-list'),
    url(r'^identifierType/(?P<pk>[0-9]+)/$', views.IdentifierTypeDetail.as_view(),name='IdentifierType-detail'),
]