from django.conf.urls import url
from .views import profile, login, logout, callback

urlpatterns = [
    url(r'profile', profile, name='profile'),
    url(r'login', login, name='login'),
    url(r'logout', logout, name='logout'),
    url(r'callback', callback, name='callback'),
]
