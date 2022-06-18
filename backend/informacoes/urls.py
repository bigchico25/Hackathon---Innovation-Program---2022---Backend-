from .api import ListBaseInformacao, ListPesquisas, Informacao

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', ListBaseInformacao.as_view(), name='home'),
    path('pesquisas', ListPesquisas.as_view(), name='pesquisas'),
    path('<int:pk>', Informacao.as_view(), name='info'),
]