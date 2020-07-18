from email_validator import validate_email

from django.db import models
from django.conf import settings

from backend.models import Model
from backend.utils import gen_random_string


class SubscriberManager(models.Manager):
    def register(self, data):
        try:
            is_valid = validate_email(data['email'])
            email = is_valid.email

        except Exception as e:
            return {'success': False, 'message': str(e)}

        if self.filter(email=email).exists():
            return {'success': False, 'message': 'This email already exists'}

        self.create(
            email=email,
            name=data['name'],
        )

        return {'success': True}

    def confirm(self, data):
        qs = self.filter(email=data['email'], token=data['token'])

        if not qs.exists():
            return {'success': False}

        else:
            obj = qs.first()
            obj.is_confirmed = True
            obj.save()

            return {'success': True}


class Message(Model):
    info = models.CharField(max_length=350, blank=True)
    content = models.TextField()

    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return self.content[:25]


class Post(Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=50, unique=True)
    teaser = models.TextField()
    content = models.TextField()

    is_hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Subscriber(Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)

    token = models.CharField(max_length=40)

    is_confirmed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = SubscriberManager()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = gen_random_string(40)

        return super(Subscriber, self).save(*args, **kwargs)

    def gen_confirmation_link(self):
        return '{}i/confirm/?email={}&token={}'.format(
            settings.FRONTEND_URL,
            self.email,
            self.token
        )
