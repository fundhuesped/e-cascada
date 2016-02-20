#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from common.models import Coding

#Clase Period
#Specialties handled by the Service Site
class Period(models.Model):
    coding = models.ForeignKey(Coding)
    text = models.TextField()
