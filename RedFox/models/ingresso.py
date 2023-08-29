from django.db import models
from RedFox.models import Categoria, Estadios, Jogos, Time

class Ingresso (models.Model):
    descricao = models.CharField (max_length=100)
    preco = models.FloatField (max_length=10000)
    quantidade = models.IntegerField (default = 1)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    jogos = models.ForeignKey(Jogos, on_delete=models.CASCADE)
    time = models.ManyToManyField (Time, related_name="+")
    estadios = models.ForeignKey(Estadios, on_delete=models.CASCADE)

    def __str__ (self):
        return self.descricao
