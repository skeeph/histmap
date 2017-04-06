# coding:utf-8
from rest_framework.serializers import ModelSerializer
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from world.models import WorldBorder


# TODO Длинный и короткий список
class CountryListSerializer(ModelSerializer):
    class Meta:
        model = WorldBorder
        fields = ('id', 'name')


class CountrySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = WorldBorder
        fields = ('id', 'name', 'iso3', 'lat','lon')
        geo_field = "mpoly"
