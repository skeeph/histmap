from django.conf.urls import url
from django.contrib.auth.views import *

from .forms import *
from .views import *

urlpatterns = [
    url(r'profile', profile, name='profile')
]
