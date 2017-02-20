from django.core.management.base import BaseCommand, CommandError
from hc_notificaciones.views import CreateNotifications
import datetime as dt
from hc_practicas.models import Turno
from hc_notificaciones.models import NotificationSMS
from hc_notificaciones.models import NotificationEmail

from django.conf import settings


class Command(BaseCommand):
    help = 'Sends turnos reminders'

    def handle(self, *args, **options):
        fetched_day = dt.date.today() + dt.timedelta(days=settings.NOTIFICATION_ANTICIPATION_DAYS)
        turnos = Turno.objects.filter(turnoSlot__day=fetched_day,
                                      state=Turno.STATE_INITIAL
                                     )
        notifications_creator = CreateNotifications()

        for turno in turnos:
            if turno.paciente.primaryPhoneNumber is not None and settings.SEND_SMS_NOTIFICATIONS:
                notifications_creator.createTurnoReminderSMSNotification(turno)

            if turno.paciente.email and settings.SEND_EMAIL_NOTIFICATIONS:
                notifications_creator.createTurnoReminderEmailNotification(turno)

            self.stdout.write(self.style.SUCCESS('Successfully sent reminders'))