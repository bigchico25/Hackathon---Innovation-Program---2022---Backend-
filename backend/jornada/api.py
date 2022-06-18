from .serializers import AtividadeSerializer
from .models import (AtividadeJornada, 
                    Jornada,
                    AlunoJornada)
from .mixins import SearchMixin
from .models import EstatisticasAcesso
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.db.models import Count, Sum


class InscreverJornada(APIView):

    def get(self, request):
        """
        """
        user = self.request.user
        jornada = Jornada.objects.first()
        AlunoJornada.objects.create(usuario=user, jornada=jornada)
        return Response({'tipo': 'sucesso'})


class MarcarAtividadeFeita(APIView):

    def get(self, request):
        """
        """
        user = self.request.user
        atividade = self.request.POST['pk']
        participacao = AlunoJornada.objects.get(usuario=user)
        participacao.atividade_feita.add(atividade)
        return Response({'tipo': 'sucesso'})


class TodasAtividadesUser(APIView):

    def get(self, request):
        """
        """
        dados = {}
        user = self.request.user
        participacao = AlunoJornada.objects.get(usuario=user)
        todas = participacao.atividade_feita.all()
        feitas = todas.values_list('pk', flat=True)
        nao_feitas = [atividade for atividade in todas if atividade not in feitas]
        atividades = AtividadeJornada.objects.all()
        atividades = AtividadeSerializer(atividades, many=True).data
        dados.update({'feitas': feitas})
        dados.update({'nao_feitas': nao_feitas})
        dados.update({'atividades': atividades})
        return Response(dados)