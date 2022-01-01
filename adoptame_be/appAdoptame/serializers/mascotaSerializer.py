from rest_framework import serializers
from appAdoptame.models.mascota import Mascota

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = ['id','especie','sexo','edad','nombre','tamaño','descripcion','personalidad','personalidades','desparasitado','esterilizado','salud', 'imagen', 'adoptado']