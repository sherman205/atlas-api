from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CustomUserSerializer
from .models import CustomUser

class CustomUserView(viewsets.ModelViewSet):
  serializer_class = CustomUserSerializer

  def get_queryset(self):
    queryset = CustomUser.objects.all()
    ID = self.request.query_params.get('id')
    username = self.request.query_params.get('username')
    if username:
      queryset = queryset.filter(username=username)
    if ID:
      queryset = queryset.filter(id=ID)
    return queryset
