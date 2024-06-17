# api/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meme, Profile

class MemeModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.meme = Meme.objects.create(
            title='Test Meme',
            description='Test Description',
            owner=self.user,
            image='test_image.png'
        )

    def test_meme_creation(self):
        self.assertEqual(self.meme.title, 'Test Meme')
        self.assertEqual(self.meme.description, 'Test Description')
        self.assertEqual(self.meme.owner, self.user)
        self.assertEqual(self.meme.image, 'test_image.png')

class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.profile = Profile.objects.create(
            user=self.user,
            bio='Test Bio',
            avatar='test_avatar.png'
        )

    def test_profile_creation(self):
        self.assertEqual(self.profile.user, self.user)
        self.assertEqual(self.profile.bio, 'Test Bio')
        self.assertEqual(self.profile.avatar, 'test_avatar.png')
