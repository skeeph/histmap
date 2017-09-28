from django.apps import apps
from django.test import TestCase

from accounts.apps import AccountsConfig
from accounts.utils import get_config


class AccountsConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(AccountsConfig.name, 'accounts')
        self.assertEqual(apps.get_app_config('accounts').name, 'accounts')


class ContextProcessorTest(TestCase):
    def test_auth0(self):
        url = '/'
        keys = ['AUTH0_DOMAIN', 'AUTH0_CLIENT_ID', 'AUTH0_CALLBACK_URL']
        cfg = get_config()
        client = self.client.get(url)
        response = str(client.content)
        for i in keys:
            self.assertIn(cfg[i], response)