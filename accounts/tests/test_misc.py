from django.apps import apps
from django.test import TestCase

from accounts.apps import AccountsConfig
from accounts.utils import get_config


class AccountsConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(AccountsConfig.name, 'accounts')
        self.assertEqual(apps.get_app_config('accounts').name, 'accounts')

