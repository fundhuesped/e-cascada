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

class CreateNotifications(generics.CreateAPIView):
    """
    Vista para generar las notificaciones de los proximos turnos
    """

    def post(self, request, *args, **kwargs):
        fetched_day = dt.date.today() + dt.timedelta(days=settings.NOTIFICATION_ANTICIPATION_DAYS)
        turnos = Turno.objects.filter(turnoSlot__day=fetched_day,
                                      state=Turno.STATE_INITIAL
                                     )

        for turno in turnos:
            if turno.paciente.primaryPhoneNumber is not None and settings.SEND_SMS_NOTIFICATIONS:
                self.createTurnoReminderSMSNotification(turno)

            if turno.paciente.email and settings.SEND_EMAIL_NOTIFICATIONS:
                self.createTurnoReminderEmailNotification(turno)

        serializer = TurnoNestSerializer(turnos, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def createTurnoReminderSMSNotification(self, turno):
        """
        Crea la notificacion de SMS y la envia
        """

        turno_slot = turno.turnoSlot
        message = "Ud. tiene un turno el " + turno_slot.day.strftime("%d/%m")
        message = message + " a las " +  turno_slot.start.strftime("%H:%M") + "hs"
        message = message + " con Dr. " + turno_slot.profesional.fatherSurname + "."
        message = message + " En caso de no poder asistir por favor cancele su turno. Muchas gracias"

        notif = NotificationSMSSerializer(data={"destination":turno.paciente.primaryPhoneNumber,
                                                "message": message,
                                                "turno": turno.id,
                                                "paciente":turno.paciente.id})
        notif.is_valid()
        notif.save()
        return notif

    def createTurnoReminderEmailNotification(self, turno):
        """
        Crea la notificacion de Email y la envia
        """

        turno_slot = turno.turnoSlot
        message = "<p>Estimado/a " + turno.paciente.firstName + " " + turno.paciente.fatherSurname + "<p>"
        message = message + "<p>Le recordamos que tiene un turno para el dia " + turno_slot.day.strftime("%d/%m/%Y")
        message = message + " a las " +  turno_slot.start.strftime("%H:%M") + "Hs."
        message = message + " con el profesional " + turno_slot.profesional.firstName + " " + turno_slot.profesional.fatherSurname + ".</p>"
        message = message + "<p>Le pedimos por favor cancelar el turno si no puede asistir.</p>"
        message = message + "<p>Muchas Gracias.</p>"

        notif = NotificationEmailSerializer(data={"message":message,
                                                  "destination":turno.paciente.email,
                                                  "title":"Recordatorio de turno",
                                                  "turno": turno.id,
                                                  "paciente":turno.paciente.id})
        notif.is_valid()
        notif.save()
        return notif
