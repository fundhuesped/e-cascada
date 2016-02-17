#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from common.models import DayOfWeek

#Segn FHIR = "Times the Service Site is available"
class AvailableTime(models.Model):
    daysOfWeek = models.ManyToManyField(DayOfWeek)                                  #mon | tue | wed | thu | fri | sat | sun
    allDay = models.BooleanField()                                                  #Always available? e.g. 24 hour service
    availableStartTime = models.TimeField()                                         #Opening time of day (ignored if allDay = true)
    availableEndTime=models.TimeField()                                             #Closing time of day (ignored if allDay = true)