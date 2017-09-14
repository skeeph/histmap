from django.conf.urls import url

from .views import world, New

urlpatterns = [
    url('new', New.as_view(), name="new_object"),
    url(r'^$', world, name='map'),

]
