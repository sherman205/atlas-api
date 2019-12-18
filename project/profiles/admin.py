from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
  list_display = ('created', 'updated', 'user_id', 'city', 'state', 'country', 'reputation_level')

admin.site.register(Profile, ProfileAdmin)
