from django.contrib import admin

# Register your models here.
from .models import Incidences

class IncidencesAdmin(admin.ModelAdmin):
    list_display = ('name','location')

admin.site.register(Incidences,IncidencesAdmin)
