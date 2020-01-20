from rest_framework import serializers

from .models import JobRole

from InvenTree.serializers import InvenTreeModelSerializer

# from part.serializers import PartBriefSerializer


class JobRoleSerializer(InvenTreeModelSerializer):
    """ Serializer for Job role object (limited detail) """

    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = JobRole
        fields = [
            'pk',
            'job_role',
        ]
