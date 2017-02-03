#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_notificaciones.models import NotificationSMS
from hc_notificaciones.models import SMSNotificationResponse
import requests
from django.conf import settings

class SMSResponseSerializer(serializers.ModelSerializer):
    """
    Serializa una respuesta de SMS
    """
    id = serializers.ReadOnlyField()

    def create(self, validated_data):

        notification = NotificationSMS.objects.get(id=validated_data.get('notification_id'))

        response = SMSNotificationResponse.objects.create(
            origin=validated_data.get('origin'),
            message=validated_data.get('message'),
            responsetype=SMSNotificationResponse.RESPONSE_TYPE_SMS,
            turno=notification.turno.id,
            paciente=notification.paciente.id,
            notification = validated_data.get('notification_id')
        )

        return response

    class Meta:
        model = SMSNotificationResponse
        fields = ('id', 'origin', 'responsetype', 'notification', 'turno', 'paciente')
