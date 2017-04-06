from rest_framework import viewsets
from rest_framework_gis.pagination import GeoJsonPagination

import api.serializers as serializers
from world.models import WorldBorder


class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.CountryListSerializer
        return serializers.CountrySerializer

    pagination_class = GeoJsonPagination
    queryset = WorldBorder.objects.all().order_by('name')
    serializer_class = serializers.CountrySerializer
