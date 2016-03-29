#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import DocumentType, SexType, Phone, Address, CivilStatusType, SocialService, EducationType


class Persona(models.Model):
    STATUS_ACTIVE = 'Active'
    STATUS_INACTIVE = 'Inactive'

    STATUS_CHOICES = (
        (STATUS_ACTIVE, 'Activo'),
        (STATUS_INACTIVE, 'Inactivo')
    )

    """
    Clase que representa la información mínima necesaria para gestionar un Documento
    """
    firstName = models.CharField(max_length=40, null=False)
    otherNames = models.CharField(max_length=60, null=True)
    fatherSurname = models.CharField(max_length=40, null=False)
    motherSurname = models.CharField(max_length=40, null=True)
    birthDate = models.DateField(null=False)
    documentType = models.ForeignKey(DocumentType, null=True)
    documentNumber = models.CharField(max_length=10, null=True)
    genderAtBirth = models.ForeignKey(SexType, on_delete=models.CASCADE, related_name='personGenderBirth', null=True)
    genderOfChoice = models.ForeignKey(SexType, on_delete=models.CASCADE, related_name='personGenderChoice', null=True)
    email = models.CharField(max_length=70, null=True)
    occupation = models.CharField(max_length=70, null=True)
    telephones = models.ForeignKey(Phone, on_delete=models.CASCADE, related_name='personPhone', null=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name='personAddress', null=False)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default=STATUS_ACTIVE)
    civilStatus = models.ForeignKey(CivilStatusType, on_delete=models.CASCADE, related_name='personCivilStatus',
                                    null=True)
    socialService = models.ForeignKey(SocialService, on_delete=models.CASCADE, related_name='personSocialService',
                                      null=True)
    socialNumber = models.CharField(max_length=40, null=True)
    education = models.ForeignKey(EducationType, on_delete=models.CASCADE, related_name='personEducation', null=True)
    terms = models.BooleanField(null=False)
