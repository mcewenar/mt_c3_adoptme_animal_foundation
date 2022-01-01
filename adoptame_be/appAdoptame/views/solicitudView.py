from django.db.models.query import QuerySet
from rest_framework import generics
from rest_framework.serializers import Serializer
#model:
from appAdoptame.models import Solicitud
#serializer:
from appAdoptame.serializers import SolicitudSerializer

#List, create
class SolicitudesListCreateView(generics.ListCreateAPIView):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer
#Crud: read, update, delete
class SolicitudRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer

 

