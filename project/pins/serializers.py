from rest_framework import serializers
from .models import Pin

class PinSerializer(serializers.ModelSerializer):

  class Meta:
    model = Pin
    fields = ('id', 'date', 'latitude', 'longitude', 'city', 'state', 'country', 'user_id')
