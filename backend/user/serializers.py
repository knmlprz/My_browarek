from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name"] ## todo add group field in the future


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):

    user = UserSerializer(required=True)
    
    class Meta:
        model = UserProfile
        fields = ["user", "weight", "height", "birthDate"]

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = User.objects.create(**user_data)
        profile = UserProfile.objects.create(user=user, **validated_data)
        return profile