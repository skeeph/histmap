from django.contrib.gis import admin as gisadmin
from .models import WorldBorder


class CountryAdmin(gisadmin.OSMGeoAdmin):
    def __init__(self, *args, **kwargs):
        super(CountryAdmin, self).__init__(*args, **kwargs)

    list_filter = ('published',)


gisadmin.site.register(WorldBorder, CountryAdmin)
