from django.contrib.gis import admin
from .models.events import Event
# Register your models here.


@admin.register(Event)
class EventAdmin(admin.OSMGeoAdmin):
    default_lon = 1400000
    default_lat = 7495000
    default_zoom = 12
