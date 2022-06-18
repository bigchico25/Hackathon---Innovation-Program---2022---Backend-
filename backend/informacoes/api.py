

from .serializers import BaseInformacaoSerializer, PesquisaSerializer
from .models import BaseInformacao, Pesquisa
from .mixins import SearchMixin
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User


class ListBaseInformacao(SearchMixin, ListAPIView):
    serializer_class = BaseInformacaoSerializer    

    def get_queryset(self, format=None):
        """
        Return a list of all infos.
        """
        dados = self.request.GET
        queryset = BaseInformacao.objects.all()
        titulo = dados.get('titulo', False)
        palavras_chave = dados.get('palavras_chave', False)
        data = dados.get('data', False)
        tipo = dados.get('tipo', False)
        autor = dados.get('autor', False)
        if titulo:
            queryset = queryset.filter(titulo__contains=titulo)
        if palavras_chave:
            queryset = queryset.filter(palavras_chave__contains=palavras_chave)
        if data:
            queryset = queryset.filter(data__gt=data)
        if tipo:
            queryset = queryset.filter(tipo__contains=tipo)
        if autor:
            queryset = queryset.filter(autor__contains=autor)
        return queryset


class ListPesquisas(ListAPIView):
    serializer_class = PesquisaSerializer    

    def get_queryset(self, format=None):
        """
        Return a list of all infos.
        """
        dados = self.request.GET
        queryset = Pesquisa.objects.all()
        cidade = dados.get('cidade', False)
        estado = dados.get('estado', False)
        ano = dados.get('ano', False)
        if cidade:
            queryset = queryset.filter(cidade__contains=cidade)
        if estado:
            queryset = queryset.filter(estado__contains=estado)
        if ano:
            queryset = queryset.filter(ano=ano)
        return queryset


class Informacao(APIView):

    def get(self, request, *args, **kwargs):
        """
        Retorna pesquisas mais acessadas.
        """
        dados = {}
        info = BaseInformacao.objects.get(pk=self.kwargs.get('pk'))
        info = BaseInformacaoSerializer(info).data
        dados.update({'informacao': info})

        return Response(dados)