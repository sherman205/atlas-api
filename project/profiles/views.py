from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProfileSerializer
from .models import Profile

class ProfileView(viewsets.ModelViewSet):
  serializer_class = ProfileSerializer

  def get_queryset(self):
    queryset = Profile.objects.all()
    city = self.request.query_params.get('city')
    if city:
      queryset = queryset.filter(city=city)
    return queryset
