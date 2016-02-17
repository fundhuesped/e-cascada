#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models

#Clase IdentifierType
#Debe contener los valores descriptos en https://www.hl7.org/fhir/v2/0203/index.html
class IdentifierType(models.Model):
    coding = models.CharField(max_length=4)
    text = models.TextField()

    class Meta:
        ordering = ['text']