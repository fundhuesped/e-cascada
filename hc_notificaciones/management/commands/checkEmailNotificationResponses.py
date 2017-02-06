from django.core.management.base import BaseCommand, CommandError
from hc_notificaciones.views import EmailNotificationResponses

from django.conf import settings


class Command(BaseCommand):
    help = 'Check email notification responses'

    def handle(self, *args, **options):
        email_notifications_responses = EmailNotificationResponses()
        email_notifications_responses.process_email_responses()
        self.stdout.write(self.style.SUCCESS('Successfully recovered responses'))