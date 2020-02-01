from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Pin
from .serializers import PinSerializer

@api_view(['GET', 'PUT'])
def pins(request, user):
  try:
    pins = Pin.objects.filter(user=user)
  except Pin.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = PinSerializer(pins, many=True)
    return Response(serializer.data)
