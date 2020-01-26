from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProfileGetSerializer, ProfilePutSerializer
from users.serializers import CustomUserGetSerializer, CustomUserPutSerializer
from .models import Profile
from users.models import CustomUser

class ProfileView(viewsets.ModelViewSet):
  serializer_class = ProfileGetSerializer

  def get_queryset(self):
    queryset = Profile.objects.all()
    ID = self.request.query_params.get('id')
    city = self.request.query_params.get('city')
    if city:
      queryset = queryset.filter(city=city)
    if ID:
      queryset = queryset.filter(id=ID)
    return queryset

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
      if 'first_name' in request.data or 'last_name' in request.data:
        user = CustomUser.objects.filter(profile=profile).first()
        user_serializer = CustomUserPutSerializer(user, data=request.data)
        if user_serializer.is_valid():
          user_serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Add logic to tie a profile to an existing user account
@api_view(['POST'])
def create_profile(request):
  serializer = ProfilePutSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)