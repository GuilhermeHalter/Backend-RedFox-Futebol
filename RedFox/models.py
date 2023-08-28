from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__ (self):
        return self.descricao

class Time(models.Model):
    nome = models.CharField(max_length=100)

    def __str__ (self):
        return self.nome

class Jogos(models.Model):
    descricao = models.CharField(max_length=100)
    time = models.ForeignKey (Time, on_delete=models.CASCADE)

    def __str__ (self):
        return self.descricao

class Estadios (models.Model):
    nome = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=100)
    jogos = models.ManyToManyField (Jogos, related_name="+")

    def __str__ (self):
        return self.nome
    


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





# Create your models here.
