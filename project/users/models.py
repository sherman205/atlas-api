from django.db import models
from django.contrib.auth.models import AbstractUser
from profiles.models import Profile

class CustomUser(AbstractUser):
  profile = models.OneToOneField(Profile, unique=True, on_delete=models.CASCADE, blank=True, null=True)

  @property
  def full_name(self):
      "Returns the person's full name."
      return '%s %s' % (self.first_name, self.last_name)

  @classmethod
  def get_profile_by_user(cls, user_id):
    return cls.objects.get(pk=user_id).profile_id

  class Meta:
    db_table = 'user'
