from django.db import models
from .utils import get_states

class Area(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nome

class Orgao(models.Model):
    ESTADO_CHOICES = get_states()
    nome = models.CharField(max_length=255)
    estado = models.CharField(max_length=2, 
                            choices=ESTADO_CHOICES,
                            null=True, blank=True)

    def __str__(self) -> str:
        return self.nome

class Tag(models.Model):
    tag = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.tag


class BaseInformacao(models.Model):
    INFORMATION_TYPE = (
        ('ART', 'Artigo'),
        ('WIK', 'Wikipédia da saúde'),
        ('NOT', 'Notícias'),
        ('PES', 'Pesquisa'),
        ('REL', 'Relatório'),
    )

    titulo = models.CharField(max_length=255)
    palavras_chave = models.ManyToManyField(Tag,
                            related_name='conteudos')
    tipo = models.CharField(max_length=4, 
                            choices=INFORMATION_TYPE)
    data_publicacao = models.DateTimeField()
    area = models.ManyToManyField(Area,
                                    related_name='conteudos')
    acessos = models.PositiveBigIntegerField(default=0,
                null=True, blank=True)
    link = models.URLField(max_length=255, 
                        null=True, blank=True)
    autor = models.CharField(max_length=255, 
                        null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.titulo

class Artigo(models.Model):
    resumo = models.TextField()
    capital_executado = models.FloatField(null=True, 
                                        blank=True)
    programa = models.CharField(max_length=255)
    informacao = models.OneToOneField(BaseInformacao,
        on_delete=models.CASCADE, 
        related_name='artigo')

    def __str__(self) -> str:
        return self.informacao.titulo

class Noticia(models.Model):
    resumo = models.TextField()
    informacao = models.OneToOneField(BaseInformacao,
        on_delete=models.CASCADE, 
        related_name='noticias')

    def __str__(self) -> str:
        return self.informacao.titulo

class WikipediaSaude(models.Model):
    texto = models.TextField()
    informacao = models.OneToOneField(BaseInformacao,
        on_delete=models.CASCADE, 
        related_name='wikipedia')

    def __str__(self) -> str:
        return self.informacao.titulo


class Avaliacao(models.Model):
    nota = models.IntegerField(default=0)
    comentario = models.TextField(null=True, blank=True)
    informacao = models.OneToOneField(BaseInformacao,
        on_delete=models.CASCADE, 
        related_name='avaliacoes')

    def __str__(self) -> str:
        return self.informacao.titulo


class Relatorio(models.Model):
    ESTADO_CHOICES = get_states()
    nota = models.IntegerField(default=0)
    comentario = models.TextField(null=True, blank=True)
    informacao = models.OneToOneField(BaseInformacao,
        on_delete=models.CASCADE, 
        related_name='relatorios')
    estado = models.CharField(max_length=2, 
                            choices=ESTADO_CHOICES,
                            null=True, blank=True)

    def __str__(self) -> str:
        return self.informacao.titulo

class Edital(models.Model):
    EDITAL_CHOICES = (
        ('CD', 'Contratação Direta'),
        ('FD', 'Fomento Descentralizado - PPSUS'),
        ('FN', 'Fomento Nacional'),
    )
    numero = models.IntegerField()
    tipo = models.CharField(max_length=2, 
        choices=EDITAL_CHOICES)
    
    def __str__(self) -> str:
        return str(self.numero) + self.tipo


class Pesquisa(models.Model):
    PESQUISA_TIPO_CHOICES = (
        ('CD', 'Contratação Direta'),
        ('FD', 'Fomento Descentralizado - PPSUS'),
        ('FN', 'Fomento Nacional'),
    )
    PESQUISA_STATUS_CHOICES = (
        ('AN', 'Em andamento'),
        ('FN', 'Finalizado')
    )
    REGIAO_CHOICES = (
        ('CE','CENTRO-OESTE'),
        ('NE','NORDESTE'),
        ('N','NORTE'),
        ('SE','SUDESTE'),
        ('S','SUL')
    )
    ESTADO_CHOICES = get_states()
    orgao = models.ForeignKey(Orgao, 
                on_delete=models.CASCADE)
    informacao = models.OneToOneField(BaseInformacao,
        on_delete=models.CASCADE, 
        related_name='pesquisas')
    estado = models.CharField(max_length=3, 
                            choices=ESTADO_CHOICES,
                            null=True, blank=True)
    regiao = models.CharField(max_length=3, 
                            choices=REGIAO_CHOICES,
                            null=True, blank=True)
    status = models.CharField(max_length=3, 
                            choices=PESQUISA_STATUS_CHOICES,
                            null=True, blank=True)
    coordenador = models.CharField(max_length=255, null=True, blank=True)
    edital = models.ForeignKey(Edital, 
        null=True, 
        blank=True, 
        on_delete=models.CASCADE)
    valor_investido = models.PositiveIntegerField(default=0)
    cidade = models.CharField(max_length=255,null=True, blank=True)
    instituicao = models.CharField(max_length=255, null=True, blank=True)
    aplicabilidade_sus = models.TextField(null=True, blank=True)
    objetivo = models.TextField(null=True, blank=True)
    metodologia = models.TextField(null=True, blank=True)
    patente = models.BooleanField(default=False)
    producoes_cientificas = models.ForeignKey(BaseInformacao, 
                                on_delete=models.CASCADE,
                                null=True, 
                                blank=True)
    tipo = models.CharField(max_length=2, 
        choices=PESQUISA_TIPO_CHOICES, 
        null=True, blank=True)

    arquivo = models.FileField(null=True)

    def __str__(self) -> str:
        return self.informacao.titulo


class Editais(models.Model):
    informacao = models.OneToOneField(BaseInformacao,
        on_delete=models.CASCADE, 
        related_name='editais')

    def __str__(self) -> str:
        return self.informacao.titulo