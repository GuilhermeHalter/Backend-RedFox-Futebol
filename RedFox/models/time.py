from django.db import models
from uploader.models import Image

class Time(models.Model):
    nome = models.CharField(max_length=100)
    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def __str__ (self):
        return self.nome