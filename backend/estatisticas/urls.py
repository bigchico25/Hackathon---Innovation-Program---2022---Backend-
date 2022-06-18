from .api import (ListPesquisasMaisAcessadas, 
                ListPesquisasMaisAcessadasPeriodo,
                ResumoPesquisas,
                ListInformacoesMaisAcessadas)

from django.urls import path

urlpatterns = [
    path('', ListPesquisasMaisAcessadas.as_view(), name='pesquisas'),
    path('periodo', ListPesquisasMaisAcessadasPeriodo.as_view(), name='pesquisas_mes'),
    path('resumo', ResumoPesquisas.as_view(), name='resumo_pesquisas'),
    path('informacoes', ListInformacoesMaisAcessadas.as_view(), name='resumo_pesquisas'),
]