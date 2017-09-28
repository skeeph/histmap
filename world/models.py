from django.contrib.gis.db import models
from datetime import date

from accounts.models import Profile


class WorldBorder(models.Model):
    creator = models.ForeignKey(Profile, related_name="countries")
    published = models.BooleanField(default=False)
    name = models.CharField(max_length=50)

    lon = models.FloatField()
    lat = models.FloatField()
    startyear = models.DateField(default=date(1000, 1, 1))
    endyear = models.DateField(null=True)

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):  # __unicode__ on Python 2
        return self.name
