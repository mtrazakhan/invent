from __future__ import unicode_literals
from django.contrib.auth.models import Permission
from django.views.generic import DetailView, ListView

from django.forms import HiddenInput

from InvenTree.views import AjaxCreateView, AjaxUpdateView, AjaxDeleteView
from InvenTree.status_codes import OrderStatus
# from InvenTree.helpers import str2bool

from .models import JobRole

from .forms import EditJobRoleForm
from django.contrib.auth import get_user_model  # Added by tasleem

User = get_user_model()  # Added by tasleem


class JobRoleIndex(ListView):
    """ View for displaying list of Job Roles
    """

    model = JobRole
    template_name = 'access/index.html'
    context_object_name = 'JobRoles'
    paginate_by = 50

    def get_queryset(self):
        queryset = JobRole.objects.all().order_by('job_role')

        return queryset


class JobRoleDetail(DetailView):
    """ Detail view for Job role object """
    context_obect_name = 'access'
    template_name = 'access/detail.html'
    queryset = JobRole.objects.all()
    model = JobRole

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['OrderStatus'] = OrderStatus

        return ctx


class JobRoleEdit(AjaxUpdateView):
    """ View for editing a Job role object """
    model = JobRole
    form_class = EditJobRoleForm
    context_object_name = 'access'
    ajax_template_name = 'modal_form.html'
    ajax_form_title = 'Edit Job Role'

    def get_data(self):
        return {
            'info': 'Edited Job Role information',
        }


class JobRoleCreate(AjaxCreateView):
    """ View for creating a new Job role object """
    model = JobRole
    context_object_name = 'access'
    form_class = EditJobRoleForm
    ajax_template_name = 'modal_form.html'
    ajax_form_title = "Create new Job Role"

    def get_data(self):
        return {
            'success': "Created new Job Role",
        }


class JobRoleDelete(AjaxDeleteView):
    """ View for deleting a Job role object """

    model = JobRole
    success_url = '/access/'
    ajax_template_name = 'access/delete.html'
    ajax_form_title = 'Delete Job Role'
    context_object_name = 'access'

    def get_data(self):
        return {
            'danger': 'Job Role was deleted',
        }
