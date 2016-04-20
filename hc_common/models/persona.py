#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import DocumentType, SexType, Location, SocialService, CivilStatusType, EducationType, ActiveModel


class Persona(ActiveModel):
    """
    Clase que representa la información mínima necesaria para gestionar un Documento
    """
    firstName = models.CharField(max_length=40, null=False)
    otherNames = models.CharField(max_length=60, null=True)
    fatherSurname = models.CharField(max_length=40, null=False)
    motherSurname = models.CharField(max_length=40, null=True)
    birthDate = models.DateField(null=True)
    documentType = models.ForeignKey(DocumentType, null=True)
    documentNumber = models.CharField(max_length=10, null=True)
    genderAtBirth = models.ForeignKey(SexType, on_delete=models.CASCADE, related_name='personGenderBirth', null=True)
    genderOfChoice = models.ForeignKey(SexType, on_delete=models.CASCADE, related_name='personGenderChoice', null=True)
    email = models.CharField(max_length=70, null=True)
    status = models.CharField(max_length=8, choices=ActiveModel.STATUS_CHOICES, default=ActiveModel.STATUS_ACTIVE)
    street = models.CharField(max_length=150, null=True)
    postal = models.CharField(max_length=10, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='personLocation', null=True)
    occupation = models.CharField(max_length=150, blank=True, null=True)
    terms = models.NullBooleanField(default=False)
    socialService = models.ForeignKey(SocialService, models.SET_NULL, blank=True, null=True)
    socialServiceNumber = models.CharField(max_length=20, null=True, blank=True)
    civilStatus = models.ForeignKey(CivilStatusType, models.SET_NULL, blank=True, null=True)
    education = models.ForeignKey(EducationType, models.SET_NULL, blank=True, null=True)
    bornPlace = models.CharField(max_length=40, null=True)
    firstVisit = models.DateField(null=True)
    notes = models.CharField(max_length=150, null=True)
    primaryPhoneNumber = models.CharField(max_length=20, null=True)
    primaryPhoneContact = models.CharField(max_length=40, null=True)
    primaryPhoneMessage = models.NullBooleanField(default=False)
    secondPhoneNumber = models.CharField(max_length=20, blank=True, null=True)
    secondPhoneContact = models.CharField(max_length=40, blank=True, null=True)
    secondPhoneMessage = models.NullBooleanField(default=False)
    thirdPhoneNumber = models.CharField(max_length=20, blank=True, null=True)
    thirdPhoneContact = models.CharField(max_length=40, blank=True, null=True)
    thirdPhoneMessage = models.NullBooleanField(default=False)
