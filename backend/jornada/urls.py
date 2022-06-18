from .api import (InscreverJornada,
                MarcarAtividadeFeita,
                TodasAtividadesUser
                )

from django.urls import path

urlpatterns = [
    path('inscricao', InscreverJornada.as_view(), name='pesquisas'),
    path('<int:pk>', MarcarAtividadeFeita.as_view(), name='pesquisas_mes'),
    path('resumo', TodasAtividadesUser.as_view(), name='resumo_pesquisas'),
]