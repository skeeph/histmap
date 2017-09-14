from auth0.v3.authentication import GetToken, Users
from django.contrib.auth import authenticate, login as do_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from flask import json

from accounts.models import Profile
from geodjango.components.auth0 import AUTH0_DOMAIN, AUTH0_CLIENT_ID, AUTH0_SECRET, AUTH0_CALLBACK_URL


@login_required
def profile(request):
    p = Profile.objects.get(user=request.user)

    return render(request, 'registration/profile.html', {
        'profile': p,
    })


def callback(request):
    code = request.GET['code']
    get_token = GetToken(AUTH0_DOMAIN)
    auth0_users = Users(AUTH0_DOMAIN)
    token = get_token.authorization_code(AUTH0_CLIENT_ID,
                                         AUTH0_SECRET, code, AUTH0_CALLBACK_URL)
    user_info = auth0_users.userinfo(token['access_token'])
    uinfo = json.loads(user_info)
    request.session['profile'] = uinfo
    user = authenticate(**uinfo)
    if user:
        do_login(request, user)
    return redirect(reverse_lazy("users:profile"))


def login(request):
    return render(request, "registration/login.html", {
        'AUTH0_DOMAIN': AUTH0_DOMAIN,
        'AUTH0_CLIENT_ID': AUTH0_CLIENT_ID,
        'AUTH0_CALLBACK_URL': AUTH0_CALLBACK_URL,
    })


# def logout(request):
#     request.session.clear()
#     parsed_base_url = urlparse(AUTH0_CALLBACK_URL)
#     base_url = parsed_base_url.scheme + '://' + parsed_base_url.netloc
#     return redirect('https://%s/v2/logout?returnTo=%s&client_id=%s' % (AUTH0_DOMAIN, base_url, AUTH0_CLIENT_ID))
