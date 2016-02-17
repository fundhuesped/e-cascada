from django.db import models

#Periodo de tiempo en el que un practicioner role es válido
#The period during which the practitioner is authorized to perform in these role(s)
class PracticionerRolePeriod(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()