#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from common.models import Identifier, HumanName, ContactPoint, Address
from practicioners.models import PracticionerRole, PracticionerQualification

class Practicioner(models.Model):
    """
    Segun HL7:
    Practitioner covers all individuals who are engaged in the healthcare process and healthcare-related services as part of their formal responsibilities and this Resource is used for attribution of activities and responsibilities to these individuals. Practitioners include (but are not limited to):

    - physicians, dentists, pharmacists
    - physician assistants, nurses, scribes
    - midwives, dietitians, therapists, optometrists, paramedics
    - medical technicians, laboratory scientists, prosthetic technicians, radiographers
    - social workers, professional home carers, official volunteers
    - receptionists handling patient registration
    - IT personnel merging or unmerging patient records
    - Service animal (e.g., ward assigned dog capable of detecting cancer in patients)

    Mas información en https://www.hl7.org/fhir/practitioner.html
    """
    #Constantes para GENDER
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    GENDER_OTHER = 'other'
    GENDER_UK = 'unknown'

    #Choices para gender
    GENDER_CHOICES = (
        (GENDER_MALE,'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_OTHER, 'Other'),
        (GENDER_UK, 'Unknown')
    )

    identifier = models.OneToOneField(Identifier, null = False)
    active = models.BooleanField(default=True)
    name = models.ForeignKey(HumanName)
    telecom = models.ManyToManyField(ContactPoint)
    address = models.ManyToManyField(Address)
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES, default=GENDER_UK)
    birthDate = models.DateTimeField(null=True)
    photo = models.URLField(null=True)
    practicionerRole = models.ManyToManyField(PracticionerRole)
    qualification = models.ManyToManyField(PracticionerQualification)
    communication = models.CharField(null=False, default="ES-AR", max_length=400) #http://tools.ietf.org/html/bcp47 separados por coma