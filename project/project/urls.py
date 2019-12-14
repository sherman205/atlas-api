from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users import views

router = routers.DefaultRouter()
router.register(r'users', views.CustomUserView, 'user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-auth/', include('rest_auth.urls')),
    path('api/v1/', include(router.urls)),
]
