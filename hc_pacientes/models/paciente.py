#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import Persona
from django.core.exceptions import ValidationError

class Paciente(Persona):
    """
    Clase que representa la información mínima necesaria para gestionar un Paciente
    """
    idpaciente = models.CharField(max_length=20, null=True)
    prospect = models.BooleanField(default=False)

    """
    Validaciones del modelo en base a si es prospecto o no
    """
    def clean(self):
        if self.primaryPhoneContact is None:
            raise ValidationError(_('El teléfono primario es obligatorio para un paciente'))
        if not self.prospect:
            if self.primaryPhoneContact is None:
                raise ValidationError(_('El contacto primario es obligatorio para un paciente'))
            if self.birthDate is None:
               raise ValidationError(_('La fecha de nacimiento es obligatoria para un paciente'))
            if self.documentNumber is None or self.documentType is None:
                raise ValidationError(_('El tipo y número de documento son obligatorios'))
            if self.genderAtBirth is None or self.genderOfChoice is None:
                raise ValidationError(_('El sexo al nacer y por elección son obligatorios'))
            if self.street is None or self.postal is None:
                raise ValidationError(_('El domicilio es obligatorio'))
            ###TODO: Ver que campos son Provincia, pertido y localidad