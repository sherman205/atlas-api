from rest_framework import serializers
from .models import CustomUser
from profiles.models import Profile

class CustomUserGetSerializer(serializers.ModelSerializer):
  full_name = serializers.ReadOnlyField()

  class Meta:
    model = CustomUser
    fields = ('id', 'email', 'username', 'first_name', 'last_name', 'full_name', 'profile_id')

class CustomUserPutSerializer(serializers.ModelSerializer):
  profile_id = serializers.IntegerField(required=False)

  class Meta:
    model = CustomUser
    fields = ('email', 'username', 'first_name', 'last_name', 'profile_id')
