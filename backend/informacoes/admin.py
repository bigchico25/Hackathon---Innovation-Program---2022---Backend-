from django.contrib import admin
from .models import (BaseInformacao, 
                    Area, 
                    Artigo, 
                    Avaliacao, 
                    Noticia, 
                    Relatorio, 
                    Tag, 
                    WikipediaSaude,
                    Orgao,
                    Pesquisa,
                    Edital)

# Register your models here.
class BaseInformacaoAdmin(admin.ModelAdmin):
    pass


class AreaAdmin(admin.ModelAdmin):
    pass

class ArtigoAdmin(admin.ModelAdmin):
    pass

class AvaliacaoAdmin(admin.ModelAdmin):
    pass

class NoticiaAdmin(admin.ModelAdmin):
    pass

class RelatorioAdmin(admin.ModelAdmin):
    pass

class TagAdmin(admin.ModelAdmin):
    pass

class WikipediaSaudeAdmin(admin.ModelAdmin):
    pass
class OrgaoSaudeAdmin(admin.ModelAdmin):
    pass
class PesquisaSaudeAdmin(admin.ModelAdmin):
    pass

class EditalSaudeAdmin(admin.ModelAdmin):
    pass


admin.site.register(BaseInformacao)
admin.site.register(Area)
admin.site.register(Artigo)
admin.site.register(Avaliacao)
admin.site.register(Noticia)
admin.site.register(Relatorio)
admin.site.register(Tag)
admin.site.register(WikipediaSaude)
admin.site.register(Orgao)
admin.site.register(Pesquisa)
admin.site.register(Edital)