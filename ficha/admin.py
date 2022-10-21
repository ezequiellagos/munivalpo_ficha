from django.contrib import admin
from .models import *


class IdentificacionInmuebleAdmin(admin.ModelAdmin):
    list_display = ('id_plano', 'rol', 'unidad_vecinal', 'comuna', 'plan_cerro_poblacion', 'denominacion_inmueble', 'autor', 'created', 'updated')
    list_filter = ('unidad_vecinal', 'comuna', 'plan_cerro_poblacion', 'autor', 'created', 'updated')
    search_fields = ('id_plano', 'rol', 'unidad_vecinal', 'comuna', 'plan_cerro_poblacion', 'denominacion_inmueble', 'autor', 'created', 'updated')

class PlanoUbicacionAdmin(admin.ModelAdmin):
    list_display = ('id_plano', 'latitud', 'longitud', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('id_plano', 'latitud', 'longitud', 'created', 'updated')

admin.site.register(IdentificacionInmueble, IdentificacionInmuebleAdmin)
admin.site.register(PlanoUbicacion, PlanoUbicacionAdmin)
admin.site.register(FotografiaGeneral)
admin.site.register(FotografiaContexto)
admin.site.register(ResenaPatrimonial)
admin.site.register(ValoracionAtributos)
admin.site.register(InformacionTecnica)

