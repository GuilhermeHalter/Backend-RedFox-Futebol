from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from RedFox.models import Ingresso
from RedFox.serializers import IngressoSerializer

class IngressoViewSet(ModelViewSet):
    queryset = Ingresso.objects.all()
    serializer_class = IngressoSerializer
    permission_classes = [IsAuthenticated]
