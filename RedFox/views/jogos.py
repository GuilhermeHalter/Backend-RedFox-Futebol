from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
#from rest_framework.permissions import IsAuthenticated

from RedFox.models import Jogos
from RedFox.serializers import JogosSerializer

class JogosViewSet(ModelViewSet):
    queryset = Jogos.objects.all()
    serializer_class = JogosSerializer
    #permission_classes = [IsAuthenticated]