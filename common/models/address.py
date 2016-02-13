from django.db import models
from .addresspointperiod import *
from .addressline import *

#Clase Address
#Segn FHIR: "A postal address. There are a variety of postal address formats defined around the world. Postal addresses are often also used to record a location that can be visited to find a patient or person."
#Ms informacin: https://www.hl7.org/fhir/datatypes.html#Address
class Address(models.Model):
    #Constantes para use
    HOME = 'home'
    WORK = 'work'
    TEMP = 'temp'
    OLD = 'old'

    #Opciones de use
    USE_CHOICES = (
        (HOME, 'Home'),
        (WORK, 'Work'),
        (TEMP, 'Temp'),
        (OLD, 'Old')
    )

    #Constantes para type
    POSTAL = 'postal'
    PHYSICAL = 'physical'
    BOTH = 'both'

    #Opciones de Type
    TYPE_CHOICES = (
        (POSTAL, 'Postal Address'),
        (PHYSICAL, 'Physical Address'),
        (BOTH, 'Physical and Postal Address')
    )

    use = models.CharField(max_length=4, choices=USE_CHOICES, default=HOME)                     #Home | work | temp | old - purpose of this address
    type = models.CharField(max_length=8, choices=TYPE_CHOICES, default=BOTH)                   #postal | physical | both
    text = models.TextField()                                                                   #Text representation of the address
    lines = models.ManyToManyField(AddressLine, related_name="lines")                           #Street name, number, direction & P.O. Box etc.
    city = models.TextField()                                                                   #Name of city, town etc.
    district = models.TextField()                                                               #District name (aka county)
    state = models.TextField()                                                                  #Sub-unit of country (abbreviations ok)
    postalCode = models.TextField()                                                             #Postal code for area
    country = models.TextField()                                                                #Country (can be ISO 3166 3 letter code)
    period = models.OneToOneField(AddressPointPeriod, related_name="period", null=True, on_delete=models.CASCADE)                                              #Time period when address was/is in use

