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
    url(r'^healthcare-service/$', views.HealthCareServiceList.as_view(), name='HealthCareService-list'),
    url(r'^healthcare-service/(?P<pk>[0-9]+)/$', views.HealthCareServiceDetails.as_view(),name='HealthCareService-detail'),
    url(r'^not-available/$', views.NotAvailableList.as_view(), name='NotAvailable-list'),
    url(r'^not-available/(?P<pk>[0-9]+)/$', views.NotAvailableDetails.as_view(),name='NotAvailable-detail'),
    url(r'^not-available-period/$', views.NotAvailablePeriodList.as_view(), name='NotAvailablePeriod-list'),
    url(r'^not-available-period/(?P<pk>[0-9]+)/$', views.NotAvailablePeriodDetails.as_view(),name='NotAvailablePeriod-detail'),
    url(r'^referral-method/$', views.ReferralMethodList.as_view(), name='ReferralMethod-list'),
    url(r'^referral-method/(?P<pk>[0-9]+)/$', views.ReferralMethodDetails.as_view(),name='ReferralMethod-detail'),
    url(r'^service-category/$', views.ServiceCategoryList.as_view(), name='ServiceCategory-list'),
    url(r'^service-category/(?P<pk>[0-9]+)/$', views.ServiceCategoryDetails.as_view(),name='ServiceCategory-detail'),
    url(r'^service-provisioning-code/$', views.ServiceProvisioningCodeList.as_view(), name='ServiceProvisioningCode-list'),
    url(r'^service-provisioning-code/(?P<pk>[0-9]+)/$', views.ServiceProvisioningCodeDetails.as_view(),name='ServiceProvisioningCode-detail'),
    url(r'^service-type/$', views.ServiceTypeList.as_view(), name='ServiceType-list'),
    url(r'^service-type/(?P<pk>[0-9]+)/$', views.ServiceTypeDetails.as_view(),name='ServiceType-detail'),
    url(r'^speciality/$', views.SpecialityList.as_view(), name='Speciality-list'),
    url(r'^speciality/(?P<pk>[0-9]+)/$', views.SpecialityDetails.as_view(),name='Speciality-detail'),
    url(r'^type-service/$', views.TypeServiceList.as_view(), name='TypeService-list'),
    url(r'^type-service/(?P<pk>[0-9]+)/$', views.TypeServiceDetails.as_view(),name='TypeService-detail'),
]