#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_notificaciones.models import BaseNotification

class NotificationEmail(BaseNotification):
    """
    Clase que representa una notificacion de Email
    """

    title = models.CharField(max_length=200)
    