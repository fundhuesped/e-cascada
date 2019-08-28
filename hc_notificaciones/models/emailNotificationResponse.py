#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_notificaciones.models import BaseNotificationResponse
from hc_notificaciones.models import NotificationEmail

class EmailNotificationResponse(BaseNotificationResponse):
    """
    Clase que representa una respuesta de notificacion Email
    """
    notification = models.ForeignKey(NotificationEmail, null=True, related_name='notification', on_delete=models.SET_NULL)
