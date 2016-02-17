#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from common.models import Coding

#Clase TypeService
#Type of service delivered or performed. Mas Info (https://www.hl7.org/fhir/valueset-c80-practice-codes.html)
class TypeService(models.Model):
    coding = models.ForeignKey(Coding)
    text = models.TextField()