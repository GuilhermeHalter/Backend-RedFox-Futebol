from django.db import models
from .time import Time

class Jogos (models.Model):
    descricao = models.CharField(max_length=100)
    time = models.ForeignKey (Time, on_delete=models.CASCADE)

    def __str__ (self):
        return self.descricao