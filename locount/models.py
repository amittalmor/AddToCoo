from django.core.urlresolvers import reverse
from django.db import models


class GeoAddress(models.Model):
    address = models.CharField(max_length=200)
    latitude = models.FloatField(default=0.0)
    longtitude = models.FloatField(default=0.0)
    count = models.IntegerField(default=0)
    
    def get_absolute_url(self):
        return reverse('locount:map',kwargs={'pk' : self.pk})
    