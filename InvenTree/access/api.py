"""
Provides a JSON API for the Company app
"""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics, permissions

from django.conf.urls import url

# from InvenTree.helpers import str2bool

from .models import JobRole
# from .models import SupplierPart, SupplierPriceBreak

from .serializers import JobRoleSerializer
# from .serializers import SupplierPartSerializer, SupplierPriceBreakSerializer


class JobRoleList(generics.ListCreateAPIView):
    """ API endpoint for accessing a list of Job role objects

    Provides two methods:

    - GET: Return list of objects
    - POST: Create a new Job role object
    """

    serializer_class = JobRoleSerializer
    queryset = JobRole.objects.all()

    permission_classes = [
        permissions.IsAuthenticated,
    ]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filter_fields = [
        'job_role',
    ]

    search_fields = [
        'job_role',
    ]

    ordering_fields = [
        'job_role',
    ]

    ordering = 'job_role'


class JobRoleDetail(generics.RetrieveUpdateDestroyAPIView):
    """ API endpoint for detail of a single Company object """

    queryset = JobRole.objects.all()
    serializer_class = JobRoleSerializer

    permission_classes = [
        permissions.IsAuthenticated,
    ]


jobRole_api_urls = [

    url(r'^(?P<pk>\d+)/?', JobRoleDetail.as_view(), name='api-jobRole-detail'),

    url(r'^.*$', JobRoleList.as_view(), name='api-jobRole-list'),
]
