from django.contrib.gis import admin as gisadmin
from .models import WorldBorder

gisadmin.site.register(WorldBorder, gisadmin.OSMGeoAdmin)
