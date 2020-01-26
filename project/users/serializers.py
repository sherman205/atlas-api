from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
  full_name = serializers.ReadOnlyField()

  class Meta:
    model = CustomUser
    fields = ('id', 'email', 'username', 'first_name', 'last_name', 'full_name', 'profile_id')

class CustomUserPutSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ('first_name', 'last_name')
