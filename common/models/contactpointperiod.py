#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models

#Periodo de tiempo en el que el identificador es valido
#La estructura sigue las definiciones de FHIR en https://www.hl7.org/fhir/datatypes.html#Period
class ContactPointPeriod(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
