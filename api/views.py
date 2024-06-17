# api/views.py
from rest_framework import viewsets
from .models import Profile, Meme, Like, Comment
from .serializers import ProfileSerializer, MemeSerializer, LikeSerializer, CommentSerializer
from django.http import HttpResponse
from .permissions import IsOwnerOrReadOnly  # Corrected import statement
from rest_framework.permissions import IsAuthenticated


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

class MemeViewSet(viewsets.ModelViewSet):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
       serializer.save(user=self.request.user)
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

def home(request):
    return HttpResponse("Welcome to the Meme Institute API")
