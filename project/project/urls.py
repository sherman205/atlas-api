from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from users import views as users_views
from profiles import views as profiles_views

router = routers.DefaultRouter()
# router.register(r'users', users_views.CustomUserView, 'user')
# router.register(r'profiles', profiles_views.ProfileView, 'profile')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    # path('api/v1/', include(router.urls)),
    url(r'^api/v1/profiles/(?P<pk>[0-9]+)/$', profiles_views.profile_detail),
    url(r'^api/v1/profiles/create/$', profiles_views.create_profile),
    url(r'^api/v1/users/(?P<pk>[0-9]+)/$', users_views.user_detail)
]
