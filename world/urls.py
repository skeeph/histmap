from django.conf.urls import url

from .views import world, new

urlpatterns = [
    url('new', new, name="new_object"),
    url(r'^$', world, name='map'),

]
