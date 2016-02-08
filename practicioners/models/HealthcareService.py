from django.db import models
from common.models import Organization, Identifier, ContactPoint
from .availabletime import AvailableTime
from .servicecategory import ServiceCategory

# Clase HealtcareService
# Define las pr�cticas que una entidad de salud puede brindar
# Seg�n FHIR: "The HealthcareService resource is used to describe a single healthcare service or category of services that are provided by an organization at a location. The location of the services could be virtual, as with TeleMedicine Services."
# Clase siguiendo las definiciones de FHIR. Mas informaci�n en : https://www.hl7.org/fhir/healthcareservice.html
class HealthcareService(models.Model):
    identifier = models.ForeignKey(Identifier, on_delete=models.CASCADE)            #External identifiers for this item
    providedBy = models.ForeignKey(Organization, on_delete=models.CASCADE)          #Organization that provides this service
    serviceCategory = models.ForeignKey(ServiceCategory, null=True, on_delete=models.SET_NULL) #Broad category of service being performed or delivered
    serviceType = models.TextField()                                                #Specific service delivered or performed TODO:Amoldar a estandar
    location = models.TextField()                                                   #Location where service may be provided TODO:Amoldar a estandar
    serviceName = models.TextField()                                                #Description of service as presented to a consumer while searching
    comment = models.TextField()                                                    #Additional description and/or any specific issues not covered elsewhere
    extraDetails = models.TextField()                                               #Extra details about the service that can't be placed in the other fields
    photo = models.TextField()                                                      #Facilitates quick identification of the service TODO:Amoldar a estandar
    telecom = models.ManyToManyField(ContactPoint)                                  #Contacts related to the healthcare service
    converageArea = models.TextField()                                              #Location(s) service is inteded for/available to TODO:Amoldar a estandar
    serviceProvisioningCode = models.TextField()                                    #Conditions under which service is available/offered TODO:Amoldar a estandar
    eligibility = models.TextField()                                                #Specific eligibility requirements required to use the service TODO:Amoldar a estandar
    eligibilityNote = models.TextField()                                            #Describes the eligibility conditions for the service
    programName = models.TextField()                                                #Program Names that categorize the service
    characteristic = models.TextField()                                             #Collection of characteristics (attributes) TODO:Amoldar a estandar
    referralMethod = models.TextField()                                             #Ways that the service accepts referrals TODO:Amoldar a estandar
    publicKey = models.TextField()                                                  #PKI Public keys to support secure communications
    appointmentRequired = models.BooleanField()                                     #If an appointment is required for access to this service
    availableTime = models.ManyToManyField(AvailableTime)                           #Times the Service Site is available
    notAvailable = models.TextField()                                               #Not available during this time due to provided reason TODO:Amoldar a estandar
    availabilityExceptions = models.TextField()                                     #Description of availability exceptions

    class Meta:
        ordering = ['serviceName']



