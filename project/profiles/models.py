from django.db import models
from users.models import CustomUser

class Profile(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  user_id = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
  city = models.CharField(max_length=128)
  state = models.CharField(max_length=2, blank=True, null=True)
  country = models.CharField(max_length=128)
  reputation_level = models.CharField(max_length=50, default='Novice')
  # profile_pic = models.ImageField()

  class Meta:
    db_table = 'profile'
