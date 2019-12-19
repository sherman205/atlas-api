from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = ('id', 'created', 'updated', 'user_id', 'city', 'state', 'country', 'reputation_level')