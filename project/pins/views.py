from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Pin
from .serializers import PinSerializer

@api_view(['GET'])
def pins(request, user):
  try:
    pins = Pin.objects.filter(user=user).order_by('date')
  except Pin.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    date = request.query_params.get('date')
    date_start = request.query_params.get('date_start')
    date_end = request.query_params.get('date_end')
    sort = request.query_params.get('sort')
    # either filter by a specific date or a range of dates
    if date:
      pins = pins.filter(date=date)
    elif date_start and date_end:
      pins = pins.filter(date__range=[date_start, date_end])

    if sort == 'DESC':
      pins = pins.order_by('-date')
    else:
      pins = pins.order_by('date')
    serializer = PinSerializer(pins, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_pin(request):
  serializer = PinSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    user_id = request.data["user_id"]
    pins = Pin.objects.filter(user=user_id)
    serializer = PinSerializer(pins, many=True)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
