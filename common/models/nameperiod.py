from django.db import models

#Periodo de tiempo en el que un nombre es valido
#La estructura sigue las definiciones de FHIR en https://www.hl7.org/fhir/datatypes.html#Period
class NamePeriod(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
