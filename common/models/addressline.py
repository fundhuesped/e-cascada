#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models

#Class AddressLine
#Street name, number, direction & P.O. Box etc.
#Clase creada para compatibilidad con el estandar FHIR, para que una Addres contenga muchas AddressLines
class AddressLine(models.Model):
    line = models.TextField()