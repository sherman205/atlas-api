from django.contrib import admin
from .models import Pin

class PinAdmin(admin.ModelAdmin):
  list_display = ('user_id', 'date', 'latitude', 'longitude', 'map_search_text', 'city', 'state', 'country')

admin.site.register(Pin, PinAdmin)
