#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_notificaciones.models import NotificationSMS
import requests
from django.conf import settings
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

class NotificationSMSSerializer(serializers.ModelSerializer):
    """
    Serializa una notificacion por SMS
    """
    id = serializers.ReadOnlyField()

    def create(self, validated_data):
        notificacion = NotificationSMS.objects.create(
            destination=validated_data.get('destination'),
            message=validated_data.get('message'),
            state=NotificationSMS.STATE_INITIAL,
            notificationtype=NotificationSMS.NOTIFICATION_TYPE_SMS,
            turno=validated_data.get('turno'),
            paciente=validated_data.get('paciente')
        )
        self.send_notification(notificacion)
        return notificacion


    def send_notification(self, notificacion):
        url = settings.BASE_SMS_URL
        url = url + "enviar_sms.asp?api=1"
        url = url + "&usuario=" + settings.SMS_SERVICE_USER
        url = url + "&clave=" + settings.SMS_SERVICE_PASSWORD
        url = url + "&tos=" + notificacion.destination
        url = url + "&texto=" + notificacion.message
        url = url + "&idinterno=​" + str(notificacion.id)
        url = url + "&respuestanumerica=1"
        response = requests.get(url)

        splitted_response = response.text.split(";")
        if splitted_response[0] == "1":
            notificacion.state = NotificationSMS.STATE_SENT
        else:
            notificacion.state = NotificationSMS.STATE_ERROR
        notificacion.save()

        return response

    class Meta:
        model = NotificationSMS
        fields = ('id', 'destination', 'message', 'state', 'turno', 'paciente')
