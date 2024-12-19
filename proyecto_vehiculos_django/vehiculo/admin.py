from django.contrib import admin
from .models import Vehiculos

# Register your models here.
@admin.register(Vehiculos)

class VehiculoAdmin(admin.ModelAdmin):
    list_display  = ('marca','modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'fecha_creacion', 'fecha_modificacion') 
    search_fields = ('marca','modelo',)