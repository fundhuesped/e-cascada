from django.conf.urls import url
from practicioners import views

app_name = "practicioners"
urlpatterns = [
    url(r'^available-time/$', views.AvailableTimeList.as_view(), name='AvailableTime-list'),
    url(r'^available-time/(?P<pk>[0-9]+)/$', views.AvailableTimeDetails.as_view(),name='AvailableTime-detail'),
    url(r'^characteristic/$', views.CharacteristicList.as_view(), name='Characteristic-list'),
    url(r'^characteristic/(?P<pk>[0-9]+)/$', views.CharacteristicDetails.as_view(),name='Characteristic-detail'),
    url(r'^eligibility/$', views.EligibilityList.as_view(), name='Eligibility-list'),
    url(r'^eligibility/(?P<pk>[0-9]+)/$', views.EligibilityDetails.as_view(),name='Eligibility-detail'),
    url(r'^referral-method/$', views.ReferralMethodList.as_view(), name='ReferralMethod-list'),
    url(r'^referral-method/(?P<pk>[0-9]+)/$', views.ReferralMethodDetails.as_view(),name='ReferralMethod-detail'),
    url(r'^service-category/$', views.ServiceCategoryList.as_view(), name='ServiceCategory-list'),
    url(r'^service-category/(?P<pk>[0-9]+)/$', views.ServiceCategoryDetails.as_view(),name='ServiceCategory-detail'),
    url(r'^service-provisioning-code/$', views.ServiceProvisioningCodeList.as_view(), name='ServiceProvisioningCode-list'),
    url(r'^service-provisioning-code/(?P<pk>[0-9]+)/$', views.ServiceProvisioningCodeDetails.as_view(),name='ServiceProvisioningCode-detail'),
    url(r'^speciality/$', views.SpecialityList.as_view(), name='Speciality-list'),
    url(r'^speciality/(?P<pk>[0-9]+)/$', views.SpecialityDetails.as_view(),name='Speciality-detail'),
    url(r'^type-service/$', views.TypeServiceList.as_view(), name='TypeService-list'),
    url(r'^type-service/(?P<pk>[0-9]+)/$', views.TypeServiceDetails.as_view(),name='TypeService-detail'),
]