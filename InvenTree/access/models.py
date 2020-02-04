from django.db import models

import random
import string


def jobId():
    stringLength = 6
    alphanumeric = string.ascii_letters + string.digits
    return ''.join(random.choice(alphanumeric) for i in range(stringLength))


class JobRole(models.Model):
    job_id = models.CharField(max_length=6, default=jobId, editable=False, help_text='Job Id', unique=True)
    job_role = models.CharField(max_length=50, help_text='Job roles')
    created_at = models.DateTimeField(auto_now_add=True, help_text='Job role created date')
    updated_at = models.DateTimeField(auto_now=True, help_text='Job roles updated date')


# class RoleUser(models.Model):
#     role_id = models.ForeignKey(JobRole, on_delete=models.CASCADE)
#     user_id = models.ForeignKey('users.User', on_delete=models.CASCADE)

# import random
# import string
#
# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.contrib.contenttypes.models import ContentType
# from django.db import models
# import rules
#
# from rules.contrib.models import RulesModel
#
#
# def uniqueId():
#     stringLength = 6
#     alphanumeric = string.ascii_letters + string.digits
#     return ''.join(random.choice(alphanumeric) for i in range(stringLength))
#
#
# class JobRole(RulesModel):
#     job_Id = models.CharField(max_length=6, primary_key=True, default=uniqueId, editable=False)
#     job_role = models.CharField(max_length=50)
#
#     class Meta:
#         rules_permissions = {
#             "add": rules.is_group_member(),
#             "read": rules.is_authenticated,
#         }
#     def __str__(self):
#         return self.job_role