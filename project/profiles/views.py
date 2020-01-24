from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# from django.shortcuts import render
# from rest_framework import viewsets
from .serializers import ProfileGetSerializer, ProfilePutSerializer
from users.serializers import CustomUserSerializer, CustomUserPutSerializer
from .models import Profile
from users.models import CustomUser

@api_view(['GET', 'PUT'])
def profile_detail(request, pk):
  try:
    profile = Profile.objects.get(pk=pk)
  except Profile.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = ProfileGetSerializer(profile)
    return Response(serializer.data)
  elif request.method == 'PUT':
    serializer = ProfilePutSerializer(profile, data=request.data)
    if serializer.is_valid():
      serializer.save()
      # if 'first_name' in request.data:
      #   user = CustomUser.objects.filter(profile=profile)
      #   user_serializer = CustomUserPutSerializer(user, data=request.data)
      #   if user_serializer.is_valid():
      #     user_serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

