import hashlib
from datetime import timedelta

from django.db import models
from django.utils import timezone


RECORD_THRESHOLD = 10 # In minutes


class HitManager(models.Manager):
    def record(self, type_=None, ua=None, ip=None, post_id=None):
        now = timezone.now()
        threshold_dt = now - timedelta(minutes=RECORD_THRESHOLD)

        if not type_ or not ua or not ip:
            return

        if not self.filter(
            type=type_,
            ua=ua,
            ip=ip,
            created__gt=threshold_dt
        ).exists():
            obj = Hit(
                type=type_,
                ua=ua,
                ip=ip
            )

            if type_ == Hit.POST_VIEW:
                obj.post_id = post_id

            obj.save()


class Hit(models.Model):
    APP_VISIT = 1
    POST_VIEW = 2

    TYPE_CHOICES = (
        (APP_VISIT, 'App visit'),
        (POST_VIEW, 'Post view'),
    )

    post = models.ForeignKey('core.Post', on_delete=models.CASCADE, null=True, blank=True)

    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, db_index=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    ua = models.CharField(max_length=1000, blank=True)
    ip = models.CharField(max_length=50, blank=True)

    hash = models.CharField(max_length=50, blank=True, db_index=True)

    objects = HitManager()

    def save(self, *args, **kwargs):
        if not self.hash:
            s = f'{self.ua}{self.ip}'.encode('ascii')
            self.hash = hashlib.sha1(s).hexdigest()[:12]

        return super(Hit, self).save(*args, **kwargs)
