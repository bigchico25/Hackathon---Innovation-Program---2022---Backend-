from cgitb import text
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Jornada(models.Model):
    titulo = models.CharField(max_length=255)


class AtividadeJornada(models.Model):
    titulo = models.CharField(max_length=255)
    ordem = models.PositiveIntegerField(default=0)
    texto = models.TextField(null=True, blank=True)
    jornada = models.ForeignKey(Jornada, 
                                on_delete=models.CASCADE, 
                                related_name='atividades',
                                null=True, blank=True)


class AlunoJornada(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    jornada = models.ForeignKey(Jornada, on_delete=models.CASCADE)
    atividade_feita = models.ManyToManyField(AtividadeJornada)