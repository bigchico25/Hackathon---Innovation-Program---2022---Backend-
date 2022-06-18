from .serializers import FatoSerializer
from .models import Fato, FakeNews
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User


class ListFatoFake(ListAPIView):
    serializer_class = FatoSerializer    

    def get_queryset(self, format=None):
        """
        Return a list of all infos.
        """
        dados = self.request.GET
        queryset = Fato.objects.all()
        titulo = dados.get('titulo', False)
        if titulo:
            queryset = queryset.filter(titulo__contains=titulo)
        return queryset