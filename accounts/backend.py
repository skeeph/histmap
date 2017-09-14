from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

from accounts.models import Profile

UserModel = get_user_model()


class Auth0Backend(ModelBackend):
    """Log in to Django without providing a password.

    """

    def authenticate(self, **kwargs):
        user_id = kwargs.get('sub', None)

        if not user_id:
            raise ValueError(_('sub can\'t be blank!'))
        username = user_id.replace('|', '-')

        try:
            return UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            user = UserModel.objects.create(username=username)
            p = Profile.objects.create(user=user, slug=user.username)
            p.save()
            return user

    def get_user(self, user_id):
        return UserModel._default_manager.get(pk=user_id)