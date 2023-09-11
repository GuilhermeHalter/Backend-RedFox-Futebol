from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from RedFox.models import Time
from RedFox.serializers import TimeSerializer

class TimeViewSet(ModelViewSet):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer
