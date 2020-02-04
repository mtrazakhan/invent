import pdb
from django.urls import reverse_lazy
from rest_framework import generics
from django.contrib.auth.models import Group



class GroupsListView(generics.ListAPIView):
    model = Group
    template_name = 'access_list.html'



class GroupsCreateView(generics.ListCreateAPIView):
    model = Group
    template_name = 'access_form.html'
    success_url = reverse_lazy('group-list')



#
# class GroupsUpdateView(generics.):
#     model = Group
#     template_name = 'access_form.html'
#     success_url = reverse_lazy('group-list')
#
#
# class GroupsDeleteView(generics.DeleteView):
#     model = Group
#     template_name = 'access_form.html'
#     success_url = reverse_lazy('group-list')