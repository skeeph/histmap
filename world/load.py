import os
from django.contrib.gis.utils import LayerMapping
from .models import WorldBorder

WORLD_MAPPING = {
    'fips': 'FIPS',
    'iso2': 'ISO2',
    'iso3': 'ISO3',
    'un': 'UN',
    'name': 'NAME',
    'area': 'AREA',
    'pop2005': 'POP2005',
    'region': 'REGION',
    'subregion': 'SUBREGION',
    'lon': 'LON',
    'lat': 'LAT',
    'mpoly': 'MULTIPOLYGON',
}

WORLD_SHP = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'TM_WORLD_BORDERS-0.3.shp'),
)


def run(verbose=True):
    layer_map = LayerMapping(
        WorldBorder, WORLD_SHP, WORLD_MAPPING,
        transform=False, encoding='iso-8859-1',
    )
    layer_map.save(strict=True, verbose=verbose)
