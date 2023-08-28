from rest_framework.serializers import ModelSerializer

from RedFox.models import Categoria, Time, Estadios, Ingresso, Jogos

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class TimeSerializer (ModelSerializer):
    class Meta:
        model = Time
        fields = "__all__"
    
class EstadiosSerializer (ModelSerializer):
    class Meta:
        model = Estadios
        fields = "__all__"
    
class IngressoSerializer (ModelSerializer):
    class Meta:
        model = Ingresso
        fields = "__all__"
    
class JogosSerializer (ModelSerializer):
    class Meta:
        model = Jogos
        fields = "__all__"
