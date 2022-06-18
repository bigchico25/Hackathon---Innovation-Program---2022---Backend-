from rest_framework import serializers
from .models import Fato, FakeNews


class FakeNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FakeNews
        fields = '__all__'


class FatoSerializer(serializers.ModelSerializer):
    fake = serializers.SerializerMethodField()

    class Meta:
        model = Fato
        fields = ('titulo', 'descricao','fake')

    def get_fake(self, obj):
        return FakeNewsSerializer(obj.fatos).data



