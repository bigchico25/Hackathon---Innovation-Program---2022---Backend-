from rest_framework import serializers


class AtividadeSerializer(serializers.Serializer):
   titulo = serializers.CharField()
   texto = serializers.TextField()
   ordem = serializers.IntegerField()