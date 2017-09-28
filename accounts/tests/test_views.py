from django.contrib.auth.models import User, AnonymousUser
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import TestCase, RequestFactory
from django.urls import reverse

from ..models import Profile
from accounts import views


class TestProfile(TestCase):
    def setUp(self):
        self.user_data = dict(
            username="testuser",
            first_name="fname_1",
            last_name="lname_1",
            email="mail@domain.com"
        )
        self.user = User.objects.create(**self.user_data)
        self.profile = Profile.objects.create(user=self.user, slug=self.user.username)
        self.factory = RequestFactory()
        self.url = reverse("users:profile")

    def test_profile(self):
        """
        Method test if profile view works fine while user is logged in.
        :return:
        """
        request = self.factory.get(self.url)
        request.user = self.user
        response = views.profile(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user_data['first_name'])
        self.assertContains(response, self.user_data['last_name'])
        self.assertContains(response, self.user_data['email'])

    def test_profile_anon(self):
        """
        Method checks that anonymous user is redirected to login page
        """
        request = self.factory.get(self.url)
        request.user = AnonymousUser()
        response = views.profile(request)
        self.assertEqual(response.status_code, 302)
        self.assertIn("location", response._headers)
        self.assertIn(reverse("users:login"), response._headers["location"][1])
        self.assertIn("?next={}".format(self.url), response._headers["location"][1])


class TestLogin(TestCase):
    def setUp(self):
        self.user_data = dict(
            username="testuser",
            first_name="fname_1",
            last_name="lname_1",
            email="mail@domain.com"
        )
        self.user = User.objects.create(**self.user_data)
        self.profile = Profile.objects.create(user=self.user, slug=self.user.username)
        self.factory = RequestFactory()
        self.url = reverse("users:login")

    def test_login(self):
        request = self.factory.get(self.url)
        request.user = AnonymousUser
        response = views.login(request)
        self.assertEqual(response.status_code, 200)

    def test_logged_in(self):
        request = self.factory.get(self.url)
        request.user = self.user
        response = views.login(request)
        self.assertEqual(response.status_code, 302)
        self.assertIn("location", response._headers)
        self.assertIn(reverse("users:profile"), response._headers["location"][1])


class TestLogout(TestCase):
    def add_session_to_request(self, request):
        """Annotate a request object with a session"""
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        return request

    def setUp(self):
        self.user_data = dict(
            username="testuser",
            first_name="fname_1",
            last_name="lname_1",
            email="mail@domain.com"
        )
        self.user = User.objects.create(**self.user_data)
        self.profile = Profile.objects.create(user=self.user, slug=self.user.username)
        self.factory = RequestFactory()
        self.url = reverse("users:login")

    def test_logout(self):
        request = self.factory.get(self.url)
        request.user = self.user
        request = self.add_session_to_request(request)
        response = views.logout(request)
        self.assertEqual(response.status_code, 302)
        self.assertIn("location", response._headers)
        self.assertIn(reverse("world:map"), response._headers["location"][1])

    def test_logout_anon(self):
        request = self.factory.get(self.url)
        request.user = AnonymousUser()
        request = self.add_session_to_request(request)
        response = views.logout(request)
        self.assertEqual(response.status_code, 302)
        self.assertIn("location", response._headers)
        self.assertIn(reverse("users:login"), response._headers["location"][1])
