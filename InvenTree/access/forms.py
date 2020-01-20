from __future__ import unicode_literals

from InvenTree.forms import HelperForm

from .models import JobRole


class EditJobRoleForm(HelperForm):
    """ Form for editing a access object """

    class Meta:
        model = JobRole
        fields = [
            'job_role_name',
        ]