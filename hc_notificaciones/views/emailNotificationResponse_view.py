#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime as dt
from hc_practicas.models import Turno
from hc_practicas.serializers import TurnoNestSerializer
from hc_notificaciones.serializers import EmailResponseSerializer
from rest_framework import generics
from rest_framework.permissions import DjangoModelPermissions

from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import imaplib
import email
import datetime


class EmailNotificationResponses(generics.RetrieveAPIView):
    """
    Vista para revisar las nuevas notificaciones de emails
    """
    mail = imaplib.IMAP4_SSL('imap.gmail.com')

    def post(self, request, *args, **kwargs):

        emails = self.get_emails()
        
        for email_uid in emails[0].split():
            result, data = self.mail.uid('fetch', email_uid, '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_string(raw_email)
            notification_id = email_message["Subject"].split("#")[1]
            origin = email_message["From"]
            message = email_message.as_string()
            email_response = EmailResponseSerializer(data={"origin":origin,
                                                           "message": message,
                                                           "notification":notification_id})
            email_response.is_valid()
            email_response.save()
        return Response({}, status=status.HTTP_201_CREATED)

    def mail_connect(self):
        mail.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        self.mail.select("inbox") # connect to inbox.

    def get_emails(self):
        if self.mail and self.mail.state is not "SELECTED":
            self.mail_connect()
        date = (datetime.date.today() - datetime.timedelta(1)).strftime("%d-%b-%Y")
        result, emails = self.mail.uid('search', None, '(SENTSINCE {date} HEADER Subject "Recordatorio de turno")'.format(date=date))
        return emails
