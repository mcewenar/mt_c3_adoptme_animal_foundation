from rest_framework import generics, views, status
from appAdoptame.models import Donante
from appAdoptame.serializers import DonanteSerializer
from rest_framework.response import Response
#average:
from django.db.models import Avg
class DonanteListCreateView(generics.ListCreateAPIView):
    queryset = Donante.objects.all()
    serializer_class = DonanteSerializer

#read, update, delete
class DonanteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Donante.objects.all()
    serializer_class = DonanteSerializer


#Promedio de donaciones
class DonanteListAverage(views.APIView):
    def get(self,request):
        aporteMonetario = Donante.objects.exclude(cantidad=0)
        queryset = aporteMonetario.aggregate(Promedio_donante=Avg('cantidad'))
        return Response(data=queryset, status=status.HTTP_200_OK)