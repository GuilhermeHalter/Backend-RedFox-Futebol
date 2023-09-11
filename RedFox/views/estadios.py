from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
#from rest_framework.permissions import IsAuthenticated

from RedFox.models import Estadios
from RedFox.serializers import EstadiosSerializer

class EstadiosViewSet(ModelViewSet):
    queryset = Estadios.objects.all()
    serializer_class = EstadiosSerializer
    #permission_classes = [IsAuthenticated]
