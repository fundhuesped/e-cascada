#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import ActiveModel
from hc_practicas.models import Turno
from hc_pacientes.models import Paciente

class BaseNotificationResponse(ActiveModel):
    """
    Clase que representa una notificacion response base
    """

    #Tipo de notificacion SMS
    RESPONSE_TYPE_SMS = 'SMS'

    #Tipo de notificacion email
    RESPONSE_TYPE_EMAIL = 'Email'

    RESPONSE_TYPE_CHOICES = (
        (RESPONSE_TYPE_SMS, 'SMS'),
        (RESPONSE_TYPE_EMAIL, 'Email')
    )

    #Accion de cancelar turno
    RESPONSE_ACTION_CANCEL = 'Cancel'

    #Accion de contar con opciones
    RESPONSE_ACTION_RESEND = 'SendOptions'

    RESPONSE_ACTION_CHOICES = (
        (RESPONSE_ACTION_CANCEL, 'Cancel'),
        (RESPONSE_ACTION_RESEND, 'SendOptions')
    )
    responsetype = models.CharField(max_length=10,
                                    choices=RESPONSE_TYPE_CHOICES,
                                    null=False)

    responseaction = models.CharField(max_length=15,
                                      choices=RESPONSE_ACTION_CHOICES,
                                      null=False)

    origin = models.CharField(max_length=100,
                              null=False)

    message = models.CharField(max_length=10000,
                               null=False)

    updated_on = models.DateField(auto_now=True)
    turno = models.ForeignKey(Turno, null=True)
    paciente = models.ForeignKey(Paciente, null=True)
