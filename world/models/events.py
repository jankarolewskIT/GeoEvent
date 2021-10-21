from django.contrib.gis.db import models


class Event(models.Model):
    name = models.CharField(max_length=128)
    point = models.PointField()
