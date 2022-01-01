from django.contrib import admin
from .models.donante import Donante
from .models.adoptante import Adoptante
from .models.mascota import Mascota
from .models.solicitud import Solicitud

# Register your models here.

#Para ver organizado el admin:
class DonanteAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('registro_donante','fecha','email','nombre','tipo_transaccion','cantidad','comentarios')
    search_fields = ['registro_donante']
    list_filter = ('fecha',)
#Demás configuraciones de la cuenta:
class MascotaAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('id','especie','edad','nombre','tamaño','descripcion','sexo','personalidad','esterilizado','desparasitado','salud','imagen')
    search_fields = ['id']
    list_filter = ('especie','tamaño','sexo')

class AdoptanteAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('cedulaAdoptante','telefono','nombre','apellido','email','edad','ciudad','direccion')
    search_fields = ['cedulaAdoptante']
    list_filter = ('nombre','apellido')

class SolicitudAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ("adoptante", "mascota", "estado", "resultado")
    search_fields = ["adoptante"]
    list_filter = ("estado", "resultado")


admin.site.register(Donante,DonanteAdmin)
admin.site.register(Adoptante, AdoptanteAdmin)
admin.site.register(Mascota, MascotaAdmin)
admin.site.register(Solicitud, SolicitudAdmin)
