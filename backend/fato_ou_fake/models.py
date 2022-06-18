from django.db import models

# Create your models here.
class FakeNews(models.Model):
    TIPO_CHOICES = (
        ('wp', 'Whatsapp'),
        ('nt', 'Notícia'),
        ('wb', 'Website'),
    )
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    tipo = models.CharField(max_length=3, choices=TIPO_CHOICES)


class Fato(models.Model):
    fake = models.ForeignKey(FakeNews, 
            related_name='fatos', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
