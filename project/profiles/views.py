from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProfileSerializer
from .models import Profile

class ProfileView(viewsets.ModelViewSet):
  serializer_class = ProfileSerializer

  def get_queryset(self):
    queryset = Profile.objects.all()
    user_id = self.request.query_params.get('user_id')
    if user_id:
      queryset = queryset.filter(user_id=user_id)
    return queryset
