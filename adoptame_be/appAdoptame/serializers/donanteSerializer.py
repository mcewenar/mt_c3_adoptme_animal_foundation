from rest_framework import serializers
from appAdoptame.models.donante import Donante

class DonanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donante
        fields = ['registro_donante','fecha','email','nombre','tipo_transaccion','cantidad','comentarios']