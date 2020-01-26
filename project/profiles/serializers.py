from rest_framework import serializers
from .models import Profile
from users.serializers import CustomUserGetSerializer

class ProfileGetSerializer(serializers.ModelSerializer):
  customuser = CustomUserGetSerializer()

  class Meta:
    model = Profile
    fields = ('id', 'city', 'state', 'country', 'reputation_level', 'customuser')

  def to_representation(self, instance):
    data = super().to_representation(instance)
    customuser = data.pop('customuser')
    if customuser:
      for key, val in customuser.items():
        if key in ('first_name', 'last_name'):
          data.update({key: val})
    return data

class ProfilePutSerializer(serializers.ModelSerializer):

  class Meta:
    model = Profile
    fields = ('id', 'city', 'state', 'country', 'reputation_level')

  def update(self, instance, validated_data):
    validated_data.pop('reputation_level', None)  # prevent reputation_level from being updated
    return super().update(instance, validated_data)
