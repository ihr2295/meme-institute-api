# api/admin.py
from django.contrib import admin
from .models import Meme, Comment, Like, Profile

admin.site.register(Meme)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Profile)
