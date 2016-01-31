from django.db import models

__author__ = 'Santi'
#Periodo de tiempo en el que el identificador es valido
#La estructura sigue las definiciones de FHIR en https://www.hl7.org/fhir/datatypes.html#Period
class ContactPointPeriod(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()

#Clase ContactPoint
#Según FHIR> Details for all kinds of technology-mediated contact points for a person or organization, including telephone, email, etc.
#Mas información: https://www.hl7.org/fhir/datatypes.html#ContactPoint
class ContactPoint(models.Model):
    #Constantes para system
    PHONE = 'phone'
    FAX = 'fax'
    EMAIL = 'email'
    PAGER = 'pager'
    FACEBOOK = 'fa' #custom value
    TWITTER = 'tw' #custom value
    OTHER = 'other'

    #Choices para system
    SYSTEM_CHOICES = (
        (PHONE, 'Phone'),
        (FAX, 'Fax'),
        (EMAIL, 'Email'),
        (PAGER, 'Pager'),
        (FACEBOOK, 'Facebook'),
        (TWITTER, 'Twitter'),
        (OTHER, 'Other')
    )

    #Constantes para use (https://www.hl7.org/fhir/valueset-contact-point-use.html)
    HOME = 'home'
    WORK = 'work'
    TEMP = 'temp'
    OLD = 'old'
    MOBILE = 'mob'

    #Choices para use
    USE_CHOICES = (
        (HOME, 'Home'),
        (WORK, 'Work'),
        (TEMP, 'Temp'),
        (OLD, 'Old'),
        (MOBILE, 'Mobile')
    )

    system = models.CharField(max_length=5, choices=SYSTEM_CHOICES, default=MOBILE)  #A system is required if a value is provided.
    value = models.TextField()                                                          #The actual contact point details
    use = models.CharField(max_length=4, choices=USE_CHOICES, default=HOME)             #home | work | temp | old | mobile - purpose of this contact point
    rank = models.PositiveIntegerField(default=1)                                       #Specify preferred order of use (1 = highest)
    period = models.ForeignKey(ContactPointPeriod, related_name='period',null=True)


