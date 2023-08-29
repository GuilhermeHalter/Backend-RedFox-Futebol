from django.db import models
from RedFox.models import Jogos

class Estadios (models.Model):
    nome = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=100)
    jogos = models.ManyToManyField (Jogos, related_name="+")

    def __str__ (self):
        return self.nome