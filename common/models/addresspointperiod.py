from django.db import models

#Periodo de tiempo en el que una direccin es valida
#La estructura sigue las definiciones de FHIR en https://www.hl7.org/fhir/datatypes.html#Period
class AddressPointPeriod(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()