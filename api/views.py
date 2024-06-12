# api/views.py
from rest_framework import viewsets
from .models import Profile, Meme, Like, Comment
from .serializers import ProfileSerializer, MemeSerializer, LikeSerializer, CommentSerializer
from django.http import HttpResponse

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class MemeViewSet(viewsets.ModelViewSet):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

def home(request):
    return HttpResponse("Welcome to the Meme Institute API")
