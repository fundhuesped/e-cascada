#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_notificaciones.models import NotificationEmail
from django.conf import settings
from django.core.mail import send_mail


class NotificationEmailSerializer(serializers.ModelSerializer):
    """
    Serializa una notificacion por SMS
    """
    id = serializers.ReadOnlyField()

    def create(self, validated_data):
        notificacion = NotificationEmail.objects.create(
            destination=validated_data.get('destination'),
            title=validated_data.get('title'),
            message=validated_data.get('message'),
            state=NotificationEmail.STATE_INITIAL,
            notificationtype=NotificationEmail.NOTIFICATION_TYPE_EMAIL,
            turno=validated_data.get('turno'),
            paciente=validated_data.get('paciente')
        )
        self.send_notification(notificacion)
        return notificacion


    def send_notification(self, notificacion):
        sucess = send_mail( notificacion.title,
                            'Un mensaje',
                            settings.EMAIL_SENDER_ADDRESS,
                            [notificacion.destination],
                            fail_silently=False,
                            html_message=notificacion.message
                          )
        if sucess == 1:
            notificacion.state = NotificationEmail.STATE_SENT
        else:
            notificacion.state = NotificationEmail.STATE_ERROR
        notificacion.save()

    class Meta:
        model = NotificationEmail
        fields = ('id', 'destination', 'title','message', 'state')
