# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
import random
import string

JOB_ROLES = (
    # ('_database_', '_visible_'),
    ('supplier', 'Supplier'),
    ('company', 'Company'),
    ('manager', 'Manager'),
    ('employee', 'Employee'),
)

USER_TYPES = (
    ('admin', 'Admin'),
    ('employee', 'Employee'),
)

USER_STATUS = (
    ('Active', 'Active'),
    ('Inactive', 'Inactive'),
)

def uniqueId():
    stringLength = 6
    alphanumeric = string.ascii_letters + string.digits
    return ''.join(random.choice(alphanumeric) for i in range(stringLength))


class User(AbstractUser):
    user_Id = models.CharField(max_length=6, default=uniqueId, editable=False, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              },
                              )

    job_role = models.CharField(max_length=50, choices=JOB_ROLES, default=False)
    # job_role = models.ForeignKey('access.JobRole', on_delete = models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=50, choices=USER_STATUS, default=True)

    # is_active = models.BooleanField(default=False)
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)
