from rest_framework import serializers
from appAdoptame.models.adoptante import Adoptante

class AdoptanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adoptante
        fields = ['cedulaAdoptante','nombre', 'apellido', 'edad', 'telefono']