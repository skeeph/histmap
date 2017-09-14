from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL)
    slug = models.SlugField(allow_unicode=True, unique=True)

    def __str__(self):
        return u'{u}\'s profile'.format(u=self.user.username)

    def __unicode__(self):
        return u'{u}\'s profile'.format(u=self.user.username)
