#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from common.models import Coding

#Clase ServiceCategory
#Son las diferentes categoras a las que puede pertenecer un servicio
class ServiceCategory(models.Model):
    coding = models.ForeignKey(Coding)
    text = models.TextField()