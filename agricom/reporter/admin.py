from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
from .models import Incidences

class IncidencesAdmin(LeafletGeoAdmin):
    list_display = ('name','location')

admin.site.register(Incidences,IncidencesAdmin)
