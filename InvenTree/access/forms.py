from __future__ import unicode_literals

from InvenTree.forms import HelperForm
from .models import JobRole
from django.contrib.auth.models import Group, Permission


class CreateJobRoleForm(HelperForm):
    """ Form for  a access object """

    class Meta:
        model = JobRole
        fields = [
            'job_role_name',
        ]


class EditJobRoleForm(HelperForm):
    """ Form for editing a access object """

    class Meta:
        model = JobRole
        fields = [
            'job_role_name',
        ]