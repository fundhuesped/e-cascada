from django.db import models
__author__ = 'Santi'

#Clase Address
#Según FHIR: "A postal address. There are a variety of postal address formats defined around the world. Postal addresses are often also used to record a location that can be visited to find a patient or person."
#Más información: https://www.hl7.org/fhir/datatypes.html#Address
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
    line = models.ManyToManyField("AddressLine")                                                  #Street name, number, direction & P.O. Box etc.
    city = models.TextField()                                                                   #Name of city, town etc.
    district = models.TextField()                                                               #District name (aka county)
    state = models.TextField()                                                                  #Sub-unit of country (abbreviations ok)
    postalCode = models.TextField()                                                             #Postal code for area
    country = models.TextField()                                                                #Country (can be ISO 3166 3 letter code)
    period = models.ForeignKey("AddressPointPeriod")                                              #Time period when address was/is in use

#Periodo de tiempo en el que una dirección es valida
#La estructura sigue las definiciones de FHIR en https://www.hl7.org/fhir/datatypes.html#Period
class AddressPointPeriod(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()

#Class AddressLine
#Street name, number, direction & P.O. Box etc.
#Clase creada para compatibilidad con el estandar FHIR, para que una Addres contenga muchas AddressLines
class AddressLine(models.Model):
    line = models.TextField()

