from django.conf.urls import url
from procedures import views

app_name = "procedures"
urlpatterns = [
    url(r'^period/$', views.PeriodList.as_view(), name='Period-list'),
]