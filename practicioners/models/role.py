#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from common.models import Coding

#Clase Role
#https://www.hl7.org/fhir/valueset-practitioner-role.html
class Role(models.Model):
    coding = models.ForeignKey(Coding)
    text = models.TextField()