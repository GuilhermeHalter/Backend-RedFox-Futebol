from rest_framework.serializers import ModelSerializer

from RedFox.models import Jogos
    
class JogosSerializer (ModelSerializer):
    class Meta:
        model = Jogos
        fields = "__all__"
