from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
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

@api_view(['GET', 'PUT'])
def user_detail(request, pk):
  try:
    user = CustomUser.objects.get(pk=pk)
  except CustomUser.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = CustomUserSerializer(user)
    return Response(serializer.data)
  elif request.method == 'PUT':
    serializer = CustomUserSerializer(user, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
