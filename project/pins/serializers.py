from rest_framework import serializers
from .models import Pin

class PinSerializer(serializers.ModelSerializer):
  user_id = serializers.IntegerField(required=True)

  class Meta:
    model = Pin
    fields = ('id', 'date', 'latitude', 'longitude', 'city', 'state', 'country', 'user_id', 'map_search_text')
