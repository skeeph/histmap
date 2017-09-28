from datetime import datetime

from rest_framework import viewsets
from rest_framework_gis.pagination import GeoJsonPagination

import api.serializers as serializers
from world.models import WorldBorder


class CountryGeoViewSet(viewsets.ReadOnlyModelViewSet):
    pagination_class = GeoJsonPagination
    queryset = WorldBorder.objects.filter(startyear__year__lte=datetime.now().year,
                                          endyear__year__gte=datetime.now().year,
                                          published=True).order_by('startyear')
    serializer_class = serializers.CountrySerializer

    def get_queryset(self):
        year = self.request.query_params.get('year', datetime.now().year)
        queryset = WorldBorder.objects.filter(startyear__year__lte=year,
                                              endyear__year__gte=year,
                                              published=True).order_by('startyear')
        return queryset


class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WorldBorder.objects.filter(startyear__year__lte=datetime.now().year,
                                          endyear__year__gte=datetime.now().year,
                                          published=True).order_by('startyear')
    serializer_class = serializers.CountryListSerializer

    def get_queryset(self):
        year = self.request.query_params.get('year', datetime.now().year)
        queryset = WorldBorder.objects.filter(startyear__year__lte=year,
                                              endyear__year__gte=year,
                                              published=True).order_by('startyear')
        return queryset
