from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils.translation import ugettext_lazy as _
# from django.conf import settings


import random
import string


def jobId(stringLength=6):
    alphanumeric = string.ascii_letters + string.digits
    return ''.join(random.choice(alphanumeric) for i in range(stringLength))
jobId = jobId(6)


class JobRole(models.Model):
    job_Id = models.CharField(max_length=6, primary_key=True, default=jobId, editable=False, help_text='Job Id')
    job_role = models.CharField(max_length=50, help_text='Job roles')
    created_at = models.DateTimeField(auto_now_add=True, help_text='Job role created date')
    updated_at = models.DateTimeField(auto_now=True, help_text='Job roles updated date')