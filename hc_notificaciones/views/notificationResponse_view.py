#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime as dt
from hc_practicas.models import Turno
from hc_practicas.serializers import TurnoNestSerializer
from hc_notificaciones.serializers import NotificationSMSSerializer
from hc_notificaciones.serializers import NotificationEmailSerializer
from hc_notificaciones.models import NotificationSMS
from hc_notificaciones.models import NotificationEmail
from rest_framework import generics
from rest_framework.permissions import DjangoModelPermissions

from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

class NotificationResponses(generics.RetrieveAPIView):
    """
    Vista para generar las notificaciones de los proximos turnos
    """

    def get(self, request, format=None):
        """
		asd
        """

        origin = request.query_params.get('origen')
        text = request.query_params.get('texto')
        notification_id = request.query_params.get('idinterno')

        print(origin)
        print(text)
        print(notification_id)

        return Response({"message": "Hello for today! See you tomorrow!"})