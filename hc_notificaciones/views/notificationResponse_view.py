#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime as dt
from hc_practicas.models import Turno
from hc_practicas.serializers import TurnoNestSerializer
from hc_notificaciones.serializers import SMSResponseSerializer
from rest_framework import generics
from rest_framework.permissions import DjangoModelPermissions

from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

class NotificationResponses(generics.CreateAPIView):
    """
    Vista para recivir respuestas de notificaciones de SMS
    """

    def get(self, request, format=None):
        """
		Servicio para recibir respuestas de SMS
        """


        origin = request.query_params.get('origen')
        message = request.query_params.get('texto')
        notification_id = request.query_params.get('idinterno')
        sms_response = SMSResponseSerializer(data={"origin":origin,
                                    			   "message": message,
                                    			   "notification":notification_id})
        sms_response.is_valid()
        sms_response.save()

        return Response(sms_response.data)
