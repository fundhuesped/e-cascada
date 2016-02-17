#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models

#Dias de la semana
class DayOfWeek(models.Model):
    #constantes de daysofWeek
    MON = 'mon'
    TUE = 'tue'
    WED = 'wed'
    THU = 'thu'
    FRI = 'fri'
    SAT = 'sat'
    SUN = 'sun'

    #Choices para daysOfWeek
    DOW_CHOICES = (
        (MON, 'Monday'),
        (TUE, 'Tuesday'),
        (WED, 'Wednesday'),
        (THU, 'Thursday'),
        (FRI, 'Friday'),
        (SAT, 'Saturday'),
        (SUN, 'Sunday')
    )
    value = models.CharField(max_length=3, choices=DOW_CHOICES, default=MON)                 #Valor del da de la semana