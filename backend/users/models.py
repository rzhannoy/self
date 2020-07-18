from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    PermissionsMixin, AbstractBaseUser, BaseUserManager
)
from django.db.models import signals

from tastypie.models import create_api_key


################
##  MANAGERS  ##
################

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        user.denormalize_token()

        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


##############
##  MODELS  ##
##############

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=50, blank=True)

    date_joined = models.DateTimeField(auto_now_add=True)

    token = models.CharField(max_length=300, blank=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.name

    def get_full_name(self):
        return self.name

    def denormalize_token(self):
        self.token = '{}:{}'.format(self.email, self.api_key.key)
        self.save()

signals.post_save.connect(create_api_key, sender=User)
