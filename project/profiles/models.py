from django.db import models

class Profile(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  on_delete=models.CASCADE
  city = models.CharField(max_length=128)
  state = models.CharField(max_length=2, blank=True, null=True)
  country = models.CharField(max_length=128)
  reputation_level = models.CharField(max_length=50, default='Novice')
  profile_pic = models.FileField(upload_to='media', blank=True)

  class Meta:
    db_table = 'profile'
