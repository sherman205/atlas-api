from django.db import models
from users.models import CustomUser

# user's reputation level min and maxes
NOVICE_MIN = 0
NOVICE_MAX = 20
EXPLORER_MIN = 21
EXPLORER_MAX = 50
WANDERLING_MIN = 51
WANDERLINg_MAX = 79
GLOBETROTTER_MIN = 80

class Pin(models.Model):
  date = models.DateTimeField(null=True, blank=True)
  latitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
  longitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  city = models.CharField(max_length=128)
  state = models.CharField(max_length=2, blank=True, null=True)
  country = models.CharField(max_length=128)

  @classmethod
  def get_pin_count_by_user(cls, user_id):
    return cls.objects.filter(user=user_id).count()

  # returns (string) a user's reputation level based on the number of pins they have
  @staticmethod
  def get_reputation_level(user_id):
    pin_count = Pin.get_pin_count_by_user(user_id)
    if pin_count >= EXPLORER_MIN and pin_count <= EXPLORER_MAX:
      return 'Explorer'
    elif pin_count >= WANDERLING_MIN and pin_count <= WANDERLINg_MAX:
      return 'Wanderling'
    elif pin_count >= GLOBETROTTER_MIN:
      return 'Globetrotter'
    else:
      return 'Novice'

  class Meta:
    db_table = 'pin'
