from rest_framework.serializers import ModelSerializer

from RedFox.models import Estadios

class EstadiosSerializer (ModelSerializer):
    class Meta:
        model = Estadios
        fields = "__all__"