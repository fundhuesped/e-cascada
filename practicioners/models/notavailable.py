#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from .notavailableperiod import NotAvailablePeriod

#Clase NotAvailable
#Not available during this time due to provided reason
class NotAvailable(models.Model):
    description = models.TextField(null=False)
    during = models.ForeignKey(NotAvailablePeriod)