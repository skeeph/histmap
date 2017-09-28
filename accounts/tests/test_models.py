from django.contrib.auth.models import User
from django.test import TestCase

from accounts.models import Profile


class ProfileTest(TestCase):
    def setUp(self):
        username = "testuser"
        self.user = User.objects.create(username=username)
        self.profile = Profile.objects.create(user=self.user, slug=username)

    def test_str(self):
        self.assertEqual(str(self.profile), "testuser's profile")

    def test_unicode(self):
        self.assertEqual(self.profile.__unicode__(), "testuser's profile")