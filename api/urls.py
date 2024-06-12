# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, MemeViewSet, LikeViewSet, CommentViewSet
from .views import home

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'memes', MemeViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', home, name='home'),
]
