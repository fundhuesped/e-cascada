#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_notificaciones.models import NotificationSMS
from hc_notificaciones.models import SMSNotificationResponse
from hc_notificaciones.serializers import NotificationSMSSerializer
from hc_practicas.models import Turno
from hc_practicas.services import turno_service

from django.conf import settings

class SMSResponseSerializer(serializers.ModelSerializer):
    """
    Serializa una respuesta de SMS
    """
    id = serializers.ReadOnlyField()

    def create(self, validated_data):

        notification = validated_data.get('notification')

        response = SMSNotificationResponse.objects.create(
            origin=validated_data.get('origin'),
            message=validated_data.get('message'),
            responsetype=SMSNotificationResponse.RESPONSE_TYPE_SMS,
            turno=notification.turno,
            paciente=notification.paciente,
            notification = notification
        )

        self.process_response(response)

        return response

    def process_response(self, response):
        if response.message.upper() == "NO":
            response.responseaction = SMSNotificationResponse.RESPONSE_ACTION_CANCEL
            if response.turno.state == Turno.STATE_INITIAL:
                turno_service.cancel_turno(response.turno, Turno.CANCELATION_PACIENT_REQUEST_SMS)
        else:
            response.responseaction = SMSNotificationResponse.RESPONSE_ACTION_RESEND
            self.send_options(response)
        response.save()
        return

    def send_options(self, response):

        message = "Por favor en caso de querer cancelar el turno envíe solo la palabra NO"

        notif = NotificationSMSSerializer(data={"destination":response.turno.paciente.primaryPhoneNumber,
                                                "message": message,
                                                "turno": response.turno.id,
                                                "paciente":response.turno.paciente.id},
                                          context={"reference_id": response.notification.id})
        notif.is_valid()
        notif.save()
        return notif

    class Meta:
        model = SMSNotificationResponse
        fields = ('id', 'message', 'origin', 'notification', 'turno', 'paciente')
