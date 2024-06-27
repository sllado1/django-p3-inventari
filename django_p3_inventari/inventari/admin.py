from django.contrib import admin
from .models import *

class ExemplarsInline(admin.TabularInline):
    model = Exemplar
    extra = 3

class PartitAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Nom", {"fields": ["nom"]}),
        ("Descripció", {"fields": ["descripcio"]}),
        ("Categoria", {"fields": ["categoria"]}),
    ]
    inlines = [ExemplarsInline]
    list_display = ["nom","descripcio","categoria"]
    search_fields = ["categoria__nom"]
    # el camp personalitzat ("resultats" o recompte de gols)
    # el mostrem com a "readonly_field"
    
admin.site.register(Categoria)
admin.site.register(Producte,PartitAdmin)
admin.site.register(Exemplar)
admin.site.register(Ubicacio)

