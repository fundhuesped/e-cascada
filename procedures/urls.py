from django.conf.urls import url
from procedures import views

app_name = "procedures"
urlpatterns = [
    url(r'^procedureperiod/$', views.ProcedurePeriodList.as_view(), name='ProcedurePeriod-list'),
    url(r'^procedureperiod/(?P<pk>[0-9]+)/$', views.ProcedurePeriodDetails.as_view(),name='ProcedurePeriod-detail'),
    url(r'^performed/$', views.PerformedList.as_view(), name='Performed-list'),
    url(r'^performed/(?P<pk>[0-9]+)/$', views.PerformedDetails.as_view(),name='Performed-detail'),
]