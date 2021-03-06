from django.core.management.base import BaseCommand
from myapp.sending import sendMail

class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            sendMail()
            self.stdout.write(self.style.SUCCESS('Emails sent!'))
        except NameError:
            self.stdout.write('error!!')
                              
