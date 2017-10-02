# coding:utf-8
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from world.models import WorldBorder


class CountrySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = WorldBorder
        fields = ('id', 'name', 'lat', 'lon')
        geo_field = "mpoly"
