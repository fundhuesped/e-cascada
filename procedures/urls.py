from django.conf.urls import url
from procedures import views

app_name = "procedures"
urlpatterns = [
    url(r'^period/$', views.PeriodList.as_view(), name='Period-list'),
    url(r'^period/(?P<pk>[0-9]+)/$', views.PeriodDetails.as_view(),name='Period-detail'),
]