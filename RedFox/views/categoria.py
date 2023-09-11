from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
#from rest_framework.permissions import IsAuthenticated

from RedFox.models import Categoria
from RedFox.serializers import CategoriaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    #permission_classes = [IsAuthenticated]