from rest_framework import serializers
from .models import Profile
from users.serializers import CustomUserSerializer

class ProfileGetSerializer(serializers.ModelSerializer):
  customuser = CustomUserSerializer()

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
