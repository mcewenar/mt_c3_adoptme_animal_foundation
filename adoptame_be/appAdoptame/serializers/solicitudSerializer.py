from rest_framework import serializers
from appAdoptame.models.solicitud import Solicitud

class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = ["id",'adoptante', 'mascota', 'estado', 'resultado']
