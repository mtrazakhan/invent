from rest_framework import serializers
# from django.contrib.auth.models import User  #Commented by tasleem
from django.contrib.auth import get_user_model #Added by tasleem

User = get_user_model() #Added by tasleem


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for a User
    """

    class Meta:
        model = User
        fields = ('pk',
                  'username',
                  'first_name',
                  'last_name',
                  'email',)
