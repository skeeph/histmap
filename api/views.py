from rest_framework import viewsets
from rest_framework_gis.pagination import GeoJsonPagination

import api.serializers as serializers
from world.models import WorldBorder


class CountryGeoViewSet(viewsets.ReadOnlyModelViewSet):
    pagination_class = GeoJsonPagination
    queryset = WorldBorder.objects.all().order_by('name')
    serializer_class = serializers.CountrySerializer

class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WorldBorder.objects.all().order_by('name')
    serializer_class = serializers.CountryListSerializer