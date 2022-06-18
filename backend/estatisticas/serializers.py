from rest_framework import serializers
from informacoes.models import BaseInformacao, Tag, Area, Artigo, Noticia, WikipediaSaude, Relatorio
from .models import EstatisticasAcesso


class MaisAcessadosSerializer(serializers.ModelSerializer):


    class Meta:
        model = BaseInformacao
        fields = ('titulo', 'acessos')


class MaisAcessadosMesSerializer(serializers.ModelSerializer):

    class Meta:
        model = EstatisticasAcesso
        fields = ('titulo', 'acessos')


class ResumoEditaisSerializer(serializers.Serializer):

   edital__tipo = serializers.CharField()
   contagem = serializers.IntegerField()


class ResumoPesquisasSerializer(serializers.Serializer):

   tipo = serializers.CharField()
   contagem = serializers.IntegerField()


class ResumoValoresSerializer(serializers.Serializer):

   tipo = serializers.CharField()
   valor = serializers.IntegerField()