from django.db import models
from .adoptante import Adoptante
from .mascota import Mascota


#Estado
# 0 Registrado
# 1 Revisando
# 3 Resultado

class Solicitud(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.IntegerField(default = 0)
    resultado = models.BooleanField(null=True)
    adoptante = models.ForeignKey(Adoptante, related_name="adoptantes",on_delete=models.SET_NULL, null=True)
    mascota = models.ForeignKey(Mascota, related_name="mascotas",on_delete=models.SET_NULL, null=True)
