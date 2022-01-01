from rest_framework import generics 
from appAdoptame.models import Mascota
from appAdoptame.serializers import MascotaSerializer

class MascotaListCreateView(generics.ListCreateAPIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer 

class MascotaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer