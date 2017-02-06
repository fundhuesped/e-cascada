#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_notificaciones.models import NotificationEmail
from hc_notificaciones.models import EmailNotificationResponse
from hc_notificaciones.serializers import NotificationEmailSerializer
from hc_practicas.models import Turno
from hc_practicas.services import turno_service
from hc_practicas.services import turnoSlot_service

from django.conf import settings

class EmailResponseSerializer(serializers.ModelSerializer):
    """
    Serializa una respuesta de SMS
    """
    id = serializers.ReadOnlyField()

    def create(self, validated_data):

        notification = validated_data.get('notification')
        response = EmailNotificationResponse.objects.create(
            origin=validated_data.get('origin'),
            message=validated_data.get('message'),
            responsetype=EmailNotificationResponse.RESPONSE_TYPE_EMAIL,
            turno=notification.turno,
            paciente=notification.paciente,
            notification = notification
        )

        self.process_response(response)

        return response

    def process_response(self, response):
        cancel_string = 'CANCELAR TURNO'
        if cancel_string in response.message.upper() :
            response.responseaction = EmailNotificationResponse.RESPONSE_ACTION_CANCEL
            if response.turno.state == Turno.STATE_INITIAL:
                turno_service.cancel_turno(response.turno, Turno.CANCELATION_PACIENT_REQUEST_EMAIL)
                if response.turno.turnoSlot.agenda:
                    turnoSlot_service.release_turno_slot(response.turno.turnoSlot)
                else:
                    turnoSlot_service.delete_turno_slot_unaware(response.turno.turnoSlot)
        else:
            response.responseaction = EmailNotificationResponse.RESPONSE_ACTION_RESEND
            self.send_options(response)
        response.save()
        return

    def send_options(self, response):

        message = "Por favor en caso de querer cancelar el turno envie solo la frase CANCELAR TURNO"

        notif = NotificationEmailSerializer(data={"destination":response.turno.paciente.email,
                                                  "message": message,
                                                  "turno": response.turno.id,
                                                  "title":"Recordatorio de turno",
                                                  "paciente":response.turno.paciente.id},
                                            context={"reference_id": response.notification.id})
        notif.is_valid()
        notif.save()
        return notif

    class Meta:
        model = EmailNotificationResponse
        fields = ('id', 'message', 'origin', 'notification', 'turno', 'paciente')
