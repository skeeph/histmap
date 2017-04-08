from django.conf.urls import url
from django.contrib.auth.views import *

from .forms import *
from .views import *

urlpatterns = [
    # login urls
    url(r'login/$',
        login,
        {'template_name': 'registration/login.html',
         'authentication_form': AuthForm,
         'redirect_authenticated_user': True},
        name='login'),
    url(r'logout/$',
        logout, {'template_name': 'registration/logout.html'},
        name='logout'),
    url(r'logout-then-login/$',
        logout_then_login,
        name='logout_then_login'),

    # change password urls
    url(r'password-change/$',
        password_change,
        {'template_name': 'registration/password_change.html', 'password_change_form': PasswordChangeForm},
        name='password_change'),
    url(r'password-change/done/$',
        password_change_done,
        {'template_name': 'registration/password_changed.html'},
        name='password_change_done'),

    # # restore password urls
    url(r'password-reset/$',
        password_reset,
        {'template_name': 'registration/password_reset.html', 'password_reset_form': PasswordResetForm},
         name='password_reset'),
    url(r'password-reset/done/$',
        password_reset_done,
        {'template_name': 'registration/password_reseted.html'},
        name='password_reset_done'),
    url(r'password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        password_reset_confirm,
        {'template_name': 'registration/password_confirm_reset.html', 'set_password_form': SetPasswordForm},
        name='password_reset_confirm'),
    url(r'password-reset/complete/$',
        password_reset_complete,
        {'template_name': 'registration/password_reset_completed.html'},
        name='password_reset_complete'),
    #
    # # Register
    # url(r'register/$', register, name='register'),
    # # url(r'edit/$', views.edit, name='edit'),
    # url(r'profile/$', profile, name='profile')
]
