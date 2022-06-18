from django.db import models
from informacoes.models import BaseInformacao


# Create your models here.
class EstatisticasAcesso(models.Model):
    informacao = models.ForeignKey(BaseInformacao, 
                        on_delete=models.CASCADE)
    data_acesso = models.DateTimeField(
        auto_now_add=True)

    def __str__(self) -> str:
        return self.informacao.titulo




