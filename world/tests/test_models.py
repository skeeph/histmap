from django.contrib.auth.models import User
from django.test import TestCase

from accounts.models import Profile
from ..models import WorldBorder


class WorldTest(TestCase):
    def setUp(self):
        """Creates test data for WorldBorser Model"""
        user = User.objects.create(username="username")
        profile = Profile.objects.create(user=user, slug="username")
        WorldBorder.objects.create(name="Nowhere",
                                   lat=0,
                                   lon=0,
                                   mpoly="MULTIPOLYGON(((743238 2967416,743238 \
                                   2967450,743265 2967450,743265.625 2967416,\
                                   743238 2967416)))",
                                   creator=profile,
                                   published=True)

    def test_str(self):
        """
        Test str method of WorldBorder
        """
        place = WorldBorder.objects.first()
        self.assertEqual(str(place), "Nowhere")
