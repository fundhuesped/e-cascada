#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from common.models import Organization, Identifier, ContactPoint
from .availabletime import AvailableTime
from .servicecategory import ServiceCategory
from .serviceprovisioningcode import ServiceProvisioningCode
from .eligibility import Eligibility
from .characteristic import Characteristic
from .referralmethod import ReferralMethod
from .servicetype import ServiceType
from .notavailable import NotAvailable

# Clase HealtcareService
# Define las prcticas que una entidad de salud puede brindar
# Segn FHIR: "The HealthcareService resource is used to describe a single healthcare service or category of services that are provided by an organization at a location. The location of the services could be virtual, as with TeleMedicine Services."
# Clase siguiendo las definiciones de FHIR. Mas informacin en : https://www.hl7.org/fhir/healthcareservice.html
class HealthcareService(models.Model):
    identifier = models.ManyToManyField(Identifier)                                             #External identifiers for this item
    providedBy = models.ForeignKey(Organization, on_delete=models.CASCADE)                      #Organization that provides this service
    serviceCategory = models.ForeignKey(ServiceCategory, null=True, on_delete=models.SET_NULL)  #Broad category of service being performed or delivered
    serviceType = models.ManyToManyField(ServiceType)                                           #Specific service delivered or performed
    location = models.TextField()                                                               #Location where service may be provided TODO:Amoldar a estandar
    serviceName = models.TextField(null=False)                                                  #Description of service as presented to a consumer while searching
    comment = models.TextField(null=True)                                                       #Additional description and/or any specific issues not covered elsewhere
    extraDetails = models.TextField(null=True)                                                  #Extra details about the service that can't be placed in the other fields
    photo = models.URLField(null=True)                                                          #Facilitates quick identification of the service (El standar lo pone como un adjunto, pero es imperformante)
    telecom = models.ManyToManyField(ContactPoint)                                              #Contacts related to the healthcare service
    coverageArea = models.TextField()                                                           #Location(s) service is inteded for/available to TODO:Amoldar a estandar
    serviceProvisioningCode = models.ManyToManyField(ServiceProvisioningCode)                   #Conditions under which service is available/offered
    eligibility = models.ForeignKey(Eligibility)                                                #Specific eligibility requirements required to use the service
    eligibilityNote = models.TextField(null=True)                                               #Describes the eligibility conditions for the service
    programName = models.TextField(null=True)                                                   #Program Names that categorize the service (el standar dice que pueden ser muchos, pero no tiene sentido)
    characteristic = models.ManyToManyField(Characteristic)                                     #Collection of characteristics (attributes)
    referralMethod = models.ManyToManyField(ReferralMethod)                                     #Ways that the service accepts referrals
    publicKey = models.TextField(null=True)                                                     #PKI Public keys to support secure communications
    appointmentRequired = models.BooleanField(default=True)                                     #If an appointment is required for access to this service
    availableTime = models.ManyToManyField(AvailableTime)                                       #Times the Service Site is available
    notAvailable = models.ManyToManyField(NotAvailable, null=True)                              #Not available during this time due to provided reason
    availabilityExceptions = models.TextField(null=True)                                        #Description of availability exceptions

    class Meta:
        ordering = ['serviceName']



