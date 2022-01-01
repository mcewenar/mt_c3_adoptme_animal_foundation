from django.conf import settings
from rest_framework import status,views, generics
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from appAdoptame.serializers.userAdminSerializer import UserAdminSerializer



from django.contrib.auth.models import User


class UserAdminListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserAdminSerializer

# Read, Update, Delete
class UserAdminRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserAdminSerializer
