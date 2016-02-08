from django.conf.urls import url
from practicioners import views

app_name = "practicioners"
urlpatterns = [
    url(r'^available-time/$', views.AvailableTimeList.as_view(), name='AvailableTime-list'),
    url(r'^available-time/(?P<pk>[0-9]+)/$', views.AvailableTimeDetails.as_view(),name='AvailableTime-detail'),
]