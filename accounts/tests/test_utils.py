from django.test import TestCase

from accounts.utils import get_config


class UtilsTest(TestCase):
    def setUp(self):
        self.cfg = get_config()

    def test_keys_count(self):
        self.assertEqual(len(self.cfg.keys()), 5)

    def test_keys(self):
        keys = list(self.cfg.keys())
        for i in ['AUTH0_CLIENT_ID', 'AUTH0_SECRET', 'AUTH0_DOMAIN', 'AUTH0_CALLBACK_URL', 'AUTH0_SUCCESS_URL']:
            self.assertIn(i, keys)