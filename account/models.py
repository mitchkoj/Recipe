####################################################
#   DESCRIPTION: custom user model based on        #
#                django's AbstractUser model       #
####################################################

from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from .manager import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    first_name = models.CharField(_('first name'), max_length=254, unique=False, null=False,
                                  blank=False, help_text= 'Required. Enter your first name')
    last_name = models.CharField(_('last name'), max_length=254, unique=False, null=False,
                                 blank=False, help_text= 'Required. Enter your last name')
    email = models.EmailField(_('email address'), unique=True, null=False, blank=False)
    email_confirmed = models.BooleanField(default=False, blank=False, null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    @staticmethod
    def get_absolute_url(uid, token):
        return reverse("activate", kwargs={'uidb64': uid, 'token': token})
