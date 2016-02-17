#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from common.models import Identifier, Organization
from practicioners.models import PracticionerQualificationPeriod

class PracticionerQualification(models.Model):
    """
    Qualifications obtained by training and certification
    """
    identifier = models.OneToOneField(Identifier)
    code = models.CharField(null=False, max_length=9) #Coded representation of the qualification
    period = models.ForeignKey(PracticionerQualificationPeriod)
    issuer = models.ForeignKey(Organization)