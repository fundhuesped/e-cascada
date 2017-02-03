#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_notificaciones.models import BaseNotificationResponse
from hc_notificaciones.models import NotificationSMS

class SMSNotificationResponse(BaseNotificationResponse):
    """
    Clase que representa una respuesta de notificacion SMS
    """
    notification = models.ForeignKey(NotificationSMS, null=True, related_name='notification')

    pass
