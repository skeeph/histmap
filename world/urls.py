from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import world, New

urlpatterns = [
    url('new', login_required(New.as_view()), name="new_object"),
    url(r'^$', world, name='map'),

]
