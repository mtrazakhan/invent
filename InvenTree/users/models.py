# -*- coding: utf-8 -*-
#Added by tasleem
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail


import random
import string


JOB_ROLES = (
    # ('_database_', '_visible_'),
    ('SUPPLIER', 'SUPPLIER'),
    ('COMPANY', 'SUPPLIER'),
    ('admin', 'Admin'),
    ('employee', 'Employee'),
)

USER_TYPES = (
    ('admin', 'Admin'),
    ('employee', 'Employee'),
)


def uniqueId():
    stringLength = 6
    alphanumeric = string.ascii_letters + string.digits
    return ''.join(random.choice(alphanumeric) for i in range(stringLength))



class User(AbstractUser):
    user_Id = models.CharField(max_length=6, default=uniqueId, editable=False, unique=True)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              },
                              )

    job_role = models.CharField(max_length=50, null=True, choices=JOB_ROLES)
    # job_role = models.ForeignKey('access.JobRole', on_delete=models.SET_NULL, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


# from django.contrib.auth.models import AbstractUser
# from django.core.mail import send_mail
#
# from django.db import models
# # import random
# # import string
# #
# #
# # def uniqueId(stringLength=6):
# #     alphanumeric = string.ascii_letters + string.digits
# #     return ''.join(random.choice(alphanumeric) for i in range(stringLength))
# # userId = uniqueId(6)
#
#
# JOB_ROLES = (
#     ('SUPPLIER', 'SUPPLIER'),
#     ('COMPANY', 'SUPPLIER'),
#     ('ADMIN', 'ADMIN'),
#     ('EMPLOYEE', 'EMPLOYEE'),
# )
#
# class User(AbstractUser):
#     # user_Id = models.CharField(max_length=6, primary_key=True, default=userId, editable=False)
#
#     email = models.EmailField(unique=True,
#                               error_messages={
#                                   'unique': "A user with that email already exists.",
#                               },
#                               )
#
#     job_role = models.CharField(max_length=50, choices=JOB_ROLES)
#     is_active = models.BooleanField(default=True)
#
#     def email_user(self, subject, message, from_email=None, **kwargs):
#         send_mail(subject, message, from_email, [self.email], **kwargs)

