from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from RedFox.models import Categoria, Jogos, Ingresso, Estadios, Time
from RedFox.serializers import CategoriaSerializer,JogosSerializer,IngressoSerializer,EstadiosSerializer,TimeSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class JogosViewSet(ModelViewSet):
    queryset = Jogos.objects.all()
    serializer_class = JogosSerializer

class IngressoViewSet(ModelViewSet):
    queryset = Ingresso.objects.all()
    serializer_class = IngressoSerializer

class EstadiosViewSet(ModelViewSet):
    queryset = Estadios.objects.all()
    serializer_class = EstadiosSerializer

class TimeViewSet(ModelViewSet):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer




# Create your views here.
