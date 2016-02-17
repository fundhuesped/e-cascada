#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from common.models import Identifier, HumanName, ContactPoint, Address, Organization, PersonLink

class Person(models.Model):
    """
    Implementada siguiendo la definicion de https://www.hl7.org/fhir/person.py.html
    """

    #Constantes para género (https://www.hl7.org/fhir/valueset-administrative-gender.html)
    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'
    UNKNOWN = 'unknown'

    #Opciones de genero
    TYPE_CHOICES = (
        (MALE, 'Masculino'),
        (FEMALE, 'Femenino'),
        (OTHER, 'Otro'),
        (UNKNOWN, 'Desconocido')
    )

    identifier = models.ForeignKey(Identifier)                                          #A human identifier for this person.py
    name = models.ForeignKey(HumanName, null=True)                                      #A name associated with the person.py
    telecom = models.ManyToManyField(ContactPoint)                                      #A contact detail for the person.py
    gender = models.CharField(max_length=7, choices=TYPE_CHOICES, default=UNKNOWN)      #male | female | other | unknown (https://www.hl7.org/fhir/valueset-administrative-gender.html)
    birthDate = models.DateField(null=True)                                             #The date on which the person.py was born
    address = models.ManyToManyField(Address)                                           #One or more addresses for the person.py
    photo = models.URLField(null=True)                                                  #Image of the person.py (el estandar dice que es un adjunto. Lo ponemos como URL para mejor gestión)
    managingOrganization = models.ForeignKey(Organization, null=True)                   #The organization that is the custodian of the person.py record
    active = models.BooleanField()                                                      #This person.py's record is in active use
    link = models.ManyToManyField(PersonLink)                                           #The resource to which this actual person.py is associated