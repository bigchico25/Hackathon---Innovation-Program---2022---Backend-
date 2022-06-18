from .serializers import (MaisAcessadosSerializer, 
                        MaisAcessadosMesSerializer,
                        ResumoEditaisSerializer,
                        ResumoPesquisasSerializer,
                        ResumoValoresSerializer,
                        )
from informacoes.models import BaseInformacao, Pesquisa
from .mixins import SearchMixin
from .models import EstatisticasAcesso
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.db.models.functions import TruncMonth
from django.db.models import Count, Sum
from django.db.models.functions import ExtractMonth

class ListInformacoesMaisAcessadas(SearchMixin, ListAPIView):
    serializer_class = MaisAcessadosSerializer    

    def get_queryset(self, format=None):
        """
        Retorna pesquisas mais acessadas.
        """
        search = self.request.GET.get('search', None)
        queryset = BaseInformacao.objects.all()\
            .order_by('-acessos')[:3]
        return queryset


class ListPesquisasMaisAcessadas(SearchMixin, ListAPIView):
    serializer_class = MaisAcessadosSerializer    

    def get_queryset(self, format=None):
        """
        Retorna pesquisas mais acessadas.
        """
        search = self.request.GET.get('search', None)
        queryset = BaseInformacao.objects.filter(tipo='PES'
                    ).order_by('-acessos')[:3]
        return queryset



class ListPesquisasMaisAcessadasPeriodo(SearchMixin, APIView):
    serializer_class = MaisAcessadosMesSerializer    


    def get(self, request):
        """
        Retorna pesquisas mais acessadas.
        """
        dados = self.request.GET
        queryset = BaseInformacao.objects.filter(tipo='PES').order_by('-acessos')[:3]
        cidade = dados.get('cidade', False)
        estado = dados.get('estado', False)
        regiao = dados.get('regiao', False)
        ano = dados.get('ano', False)
        if cidade:
            queryset = queryset.filter(cidade=cidade)
        if estado:
            queryset = queryset.filter(estado=estado)
        if ano:
            queryset = queryset.filter(ano=ano)
        if regiao:
            queryset = queryset.filter(regiao=regiao)
        lista_mais_acessadas = []
        for pk in queryset.values_list('pk', flat=True):
            acesso = EstatisticasAcesso.objects.filter(informacao__id=pk)\
                .annotate(month=ExtractMonth('data_acesso'))\
                .values('month', 'informacao__titulo')  \
                .annotate(contagem = Count('id'))\
                .values('informacao__titulo', 'month', 'contagem')\
                .order_by('contagem')
            lista_mais_acessadas.append(acesso)
        resultado = []
        for _queryset in lista_mais_acessadas:
            for value in _queryset:
                dictionary = {'titulo': value['informacao__titulo'],
                            'mes': value['month'],
                            'acesso': value['contagem']}
            resultado.append(dictionary)
        resultado.sort(reverse=True, key=lambda x: x['acesso'])
        return Response({'resultado': resultado})



class ResumoPesquisas(SearchMixin, APIView):

    def get(self, request):
        """
        Retorna pesquisas mais acessadas.
        """
        dados = {}
        data = self.request.GET
        queryset = Pesquisa.objects.all()
        cidade = data.get('cidade', False)
        estado = data.get('estado', False)
        regiao = data.get('regiao', False)
        ano = data.get('ano', False)
        if cidade:
            queryset = queryset.filter(cidade=cidade)
        if estado:
            queryset = queryset.filter(estado=estado)
        if ano:
            queryset = queryset.filter(ano=ano)
        if regiao:
            queryset = queryset.filter(regiao=regiao)

        modalidades_editais = queryset.values('edital__tipo') \
            .annotate(contagem = Count('edital__tipo')) \
            .order_by('-contagem')
        modalidades_editais = [value for value in modalidades_editais]
        modalidades_editais = ResumoEditaisSerializer(modalidades_editais, many=True).data
        dados.update({'modalidades_editais': modalidades_editais})

        modalidades_pesquisas = queryset.values('tipo') \
            .annotate(contagem = Count('tipo')) \
            .order_by('-contagem')
        modalidades_pesquisas = [value for value in modalidades_pesquisas]
        modalidades_pesquisas = ResumoPesquisasSerializer(modalidades_pesquisas, many=True).data
        dados.update({'modalidades_pesquisas': modalidades_pesquisas})

        modalidades_valores = queryset.values('tipo') \
            .annotate(valor = Sum('valor_investido')) \
            .order_by('-valor')
        modalidades_valores = [value for value in modalidades_valores]
        modalidades_valores = ResumoValoresSerializer(modalidades_valores, many=True).data
        dados.update({'modalidades_valores': modalidades_valores})

        return Response(dados)

