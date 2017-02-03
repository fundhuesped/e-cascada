#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import ActiveModel
from hc_practicas.models import Turno
from hc_pacientes.models import Paciente

class BaseNotification(ActiveModel):
    """
    Clase que representa una notificacion base
    """

    #Estado inicial de la notificacion
    STATE_INITIAL = 'Initial'

    #La notificacion ya fue enviada
    STATE_SENT = 'Sent'

    #La notificacion no pudo ser enviada por un error
    STATE_ERROR = 'Error'

    #Tipo de notificacion SMS
    NOTIFICATION_TYPE_SMS = 'SMS'

    #Tipo de notificacion email
    NOTIFICATION_TYPE_EMAIL = 'Email'

    STATE_CHOICES = (
        (STATE_INITIAL, 'Inicial'),
        (STATE_SENT, 'Enviada'),
        (STATE_ERROR, 'Error')
    )

    NOTIFICATION_TYPE_CHOICES = (
        (NOTIFICATION_TYPE_SMS, 'SMS'),
        (NOTIFICATION_TYPE_EMAIL, 'Email')
    )


    state = models.CharField(max_length=10,
                             choices=STATE_CHOICES,
                             null=False,
                             default=STATE_INITIAL)

    notificationtype = models.CharField(max_length=10,
                                        choices=NOTIFICATION_TYPE_CHOICES,
                                        null=False)

    destination = models.CharField(max_length=100,
                                   null=False)

    message = models.CharField(max_length=10000,
                               null=False)

    updated_on = models.DateField(auto_now=True)
    turno = models.ForeignKey(Turno, null=True, related_name='turno')
    paciente = models.ForeignKey(Paciente, null=True)
