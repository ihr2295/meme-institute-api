#memeinstitute/urls.py 

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import MemeViewSet, ProfileViewSet

router = DefaultRouter()
router.register(r'memes', MemeViewSet)
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
]