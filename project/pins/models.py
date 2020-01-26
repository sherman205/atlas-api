from django.db import models
from users.models import CustomUser

class Profile(models.Model):
  date = models.DateTimeField(null=True, blank=True)
  latitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
  longitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
  user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  city = models.CharField(max_length=128)
  state = models.CharField(max_length=2, blank=True, null=True)
  country = models.CharField(max_length=128)

  class Meta:
    db_table = 'pin'
