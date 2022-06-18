from rest_framework import serializers
from .models import BaseInformacao, Tag, Area, Artigo, Noticia, WikipediaSaude, Relatorio, Pesquisa


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'

class AreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Area
        fields = '__all__'

class ArtigoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artigo
        fields = '__all__'

class NoticiaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Noticia
        fields = '__all__'

class WikipediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = WikipediaSaude
        fields = '__all__'

class RelatorioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Relatorio
        fields = '__all__'

class PesquisaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pesquisa
        fields = '__all__'


class BaseInformacaoSerializer(serializers.ModelSerializer):
    palavras_chave = TagSerializer(many=True, read_only=True)
    area = AreaSerializer(many=True, read_only=True)
    conteudo = serializers.SerializerMethodField()

    class Meta:
        model = BaseInformacao
        fields = ('titulo', 'palavras_chave', 'area', 'tipo', 'data_publicacao', \
            'acessos', 'link', 'autor', 'data_criacao', 'conteudo')

    def get_conteudo(self, obj):
        classes = {
            'ART': 'ArtigoSerializer(obj.artigo)',
            'NOT': 'NoticiaSerializer(obj.noticias)',
            'WIK': 'WikipediaSerializer(obj.wikipedia)',
            'REL': 'RelatorioSerializer(obj.relatorios)',
            'PES': 'PesquisaSerializer(obj.pesquisas)',
        }
        dados = classes.get(obj.tipo, [])
        return eval(dados).data


class PesquisaSerializer(serializers.ModelSerializer):
    titulo = serializers.SerializerMethodField()
    class Meta:
        model = Pesquisa
        fields = ('titulo', 'coordenador', 'objetivo')
    
    def get_titulo(self, obj):
        return obj.informacao.titulo

