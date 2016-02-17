#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models

#Service not available between these dates
#La estructura sigue las definiciones de FHIR en https://www.hl7.org/fhir/datatypes.html#Period
class NotAvailablePeriod(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()