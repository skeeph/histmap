from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.utils.text import slugify

from accounts.models import Profile

UserModel = get_user_model()


class Auth0Backend(ModelBackend):
    """Log in to Django without providing a password.

    """

    def authenticate(self, **kwargs):
        user_id = kwargs.get('sub', None)
        first_name = kwargs.get('given_name', "")
        last_name = kwargs.get('family_name', "")

        if not user_id:
            raise ValueError(_('sub can\'t be blank!'))
        username = user_id.replace('|', '-')

        try:
            return UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            user = UserModel.objects.create(username=username,
                                            first_name=first_name,
                                            last_name=last_name)
            user.save()
            user_profile = Profile.objects.create(user=user,
                                                  slug=slugify('{f} {l}'.
                                                               format(f=user.first_name,
                                                                      l=user.last_name),
                                                               allow_unicode=True))
            user_profile.save()
            return user

    def get_user(self, user_id):
        return UserModel.objects.get(pk=user_id)
