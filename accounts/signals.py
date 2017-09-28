from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.utils.text import slugify

from accounts.models import Profile


@receiver(user_signed_up)
def create_profile(user):
    Profile.objects.create(user=user,
                           slug=slugify('{f} {l}'.
                                        format(f=user.first_name,
                                               l=user.last_name),
                                        allow_unicode=True))
