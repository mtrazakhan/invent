# -*- coding: utf-8 -*-
#Added by tasleem
from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils.translation import ugettext_lazy as _
# from django.conf import settings
from django.core.mail import send_mail


import random
import string


def uniqueId(stringLength=6):
    alphanumeric = string.ascii_letters + string.digits
    return ''.join(random.choice(alphanumeric) for i in range(stringLength))
userId = uniqueId(6)


class User(AbstractUser):
    user_Id = models.CharField(max_length=6, primary_key=True, default=userId, editable=False)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              },
                              )

    job_role = models.CharField(max_length=50, null=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)
#
# class UserProfile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
#     title = models.CharField(max_length=200)
#     dob = models.DateField()
#     address = models.CharField(max_length=255)
#     country = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)
#     zip = models.CharField(max_length=5)
#     photo = models.ImageField(upload_to='uploads', blank=True)

