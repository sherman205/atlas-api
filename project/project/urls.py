from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users import views as users_views
from profiles import views as profiles_views

router = routers.DefaultRouter()
router.register(r'users', users_views.CustomUserView, 'user')
router.register(r'profiles', profiles_views.ProfileView, 'profile')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/v1/', include(router.urls)),
]
