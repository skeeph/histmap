import json

from auth0.v3.authentication import GetToken, Users
from django.conf import settings
from django.contrib.auth import authenticate, login as do_login, logout as do_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from accounts.models import Profile
from django.conf import settings


@login_required
def profile(request):
    """
    User profile. Show countries added by users
    """
    user_profile = Profile.objects.get(user=request.user)

    return render(request, 'registration/profile.html', {
        'profile': user_profile,
    })


def callback(request):
    """
    Auth0 callback view
    """
    code = request.GET['code']
    get_token = GetToken(settings.AUTH0_DOMAIN)
    auth0_users = Users(settings.AUTH0_DOMAIN)
    token = get_token.authorization_code(settings.AUTH0_CLIENT_ID,
                                         settings.AUTH0_SECRET, code, settings.AUTH0_CALLBACK_URL)
    user_info = auth0_users.userinfo(token['access_token'])
    uinfo = json.loads(user_info)
    request.session['profile'] = uinfo
    user = authenticate(**uinfo)
    if user:
        do_login(request, user)
    return redirect(reverse_lazy("users:profile"))


def login(request):
    """
    Login by Auth0. If user is logged in, he is redirected to profile page
    """
    if not request.user.is_anonymous:
        return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        return render(request, "registration/login.html")


def logout(request):
    """
        If user isn't logged in, he is redirected to login page
        """
    if request.user.is_anonymous:
        return redirect(reverse_lazy("users:login"))
    else:
        do_logout(request)
        request.session.clear()
        return redirect(reverse_lazy("world:map"))
