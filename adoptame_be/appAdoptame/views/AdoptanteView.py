from django.conf import settings
from rest_framework import generics
#from rest_framework.response import Response
#from rest_framework.serializers import Serializer
#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
#from rest_framework_simplejwt.backends import TokenBackend
#from rest_framework.permissions import IsAuthenticated
from appAdoptame.models.adoptante import Adoptante
from appAdoptame.serializers.adoptanteSerializer import AdoptanteSerializer


#class AdoptanteView(views.APIView):
#
#    permission_classes = (IsAuthenticated,)
#    def post(self, request, *args, **kwargs):
#        serializer = AdoptanteSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            data = {"message": "Se creo un adoptante"}
#            return Response(data=data, status=status.HTTP_201_CREATED)
#        else:
#            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#    def get(self, request, *args, **kwargs):
#        querySet = Adoptante.objects.all()
#        serializer_class = AdoptanteSerializer(querySet, many=True)
#        return Response(data=serializer_class.data,status=status.HTTP_200_OK)


# List, Create
class AdoptanteListCreateView(generics.ListCreateAPIView):
    queryset = Adoptante.objects.all()
    serializer_class = AdoptanteSerializer

# Read, Update, Delete
class AdoptanteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Adoptante.objects.all()
    serializer_class = AdoptanteSerializer