from django.contrib import admin
from .models import (EstatisticasAcesso, )

# Register your models here.
class EstatisticasAcessoAdmin(admin.ModelAdmin):
    pass



admin.site.register(EstatisticasAcesso)
