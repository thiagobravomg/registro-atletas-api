from django.contrib import admin
from .models import Atleta

@admin.register(Atleta)
class AtletaAdmin(admin.ModelAdmin):
    list_display = ['nome','equipe']
    list_filter = ['idade','genero','peso','graduacao']