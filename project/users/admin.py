from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    UserAdmin.list_display += ('profile_id',)
    UserAdmin.list_filter += ('profile_id',)
    UserAdmin.fieldsets += (('profile_id', {'fields': ('profile',)}),)

admin.site.register(CustomUser, CustomUserAdmin)
