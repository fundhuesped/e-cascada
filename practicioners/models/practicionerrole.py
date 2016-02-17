#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from common.models import Organization, Location
from practicioners.models import Speciality, Role, PracticionerRolePeriod, HealthcareService

class PracticionerRole(models.Model):
    """
    Según HL7: Roles/organizations the practitioner is associated with.
    """
    managingOrganization = models.ForeignKey(Organization)
    role = models.ForeignKey(Role) #Valores posibles: https://www.hl7.org/fhir/valueset-practitioner-role.html
    speciality = models.ManyToManyField(Speciality)
    period = models.ForeignKey(PracticionerRolePeriod)
    location = models.ManyToManyField(Location)
    healthCareService = models.ManyToManyField(HealthcareService)
