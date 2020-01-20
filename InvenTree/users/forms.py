# from django import forms
# from django.contrib.auth import get_user_model
# from InvenTree.forms import HelperForm
# from django.contrib.auth.forms import UserCreationForm as AuthUserCreationForm
#
#
# User = get_user_model()
#
#
# class UserCreationForm(AuthUserCreationForm, HelperForm):
#
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'username', 'email', 'job_role')
#
#
# class UserUpdateForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'username', 'email', 'job_role')