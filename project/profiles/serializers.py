from rest_framework import serializers
from .models import Profile
from users.serializers import CustomUserSerializer

class ProfileSerializer(serializers.ModelSerializer):
  customuser = CustomUserSerializer()

  class Meta:
    model = Profile
    fields = ('city', 'state', 'country', 'reputation_level', 'customuser')

  def to_representation(self, instance):
    data = super(ProfileSerializer, self).to_representation(instance)
    customuser = data.pop('customuser')
    if customuser:
      for key, val in customuser.items():
        if key in ('first_name', 'last_name'):
          data.update({key: val})
    return data
