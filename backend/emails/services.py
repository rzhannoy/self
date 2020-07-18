from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .tasks import send_email as send_email_async


class Mailer(object):
    def send_email(self, email, force=False):
        if not settings.DEBUG or force:
            send_email_async.delay(email)

    def send_test(self):
        email = EmailMultiAlternatives(
            'From Rzhannoy to Nick Ten',
            'Hi, Nick. Please confirm your email. Regards, @rzhannoy',
            settings.DEFAULT_FROM_EMAIL,
            ['nrzhannoy@gmail.com']
        )

        self.send_email(email, True)

    def send_confirmation_email(self, subscriber):
        subject = 'Welcome to Rzhannoy'
        body = render_to_string('emails/confirmation.txt', {
            'name': subscriber.name,
            'link': subscriber.gen_confirmation_link(),
        })

        email = EmailMultiAlternatives(
            subject, body, settings.DEFAULT_FROM_EMAIL, [subscriber.email]
        )

        self.send_email(email)
