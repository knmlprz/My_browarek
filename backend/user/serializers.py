from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "groups"]


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):

    user = UserSerializer(required=True)
    
    class Meta:
        model = UserProfile
        fields = ["user", "weight", "height", "birthDate"]

