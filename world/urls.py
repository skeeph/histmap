from django.conf.urls import url

from .views import world

urlpatterns = [
    url(r'^$', world, name='index'),

]
