from django.contrib import admin
from api.models.financiadores import Financiadores
from api.models.projetos import Projetos
from api.models.areas_tecnologicas import AreasTecnologicas
from api.models.colaboradores import Colaboradores

@admin.register(Financiadores)
class FinanciadoresAdmin(admin.ModelAdmin):
    list_display = ("id_financiador", "financiador")
    search_fields = ("financiador",)
    ordering = ("financiador",)

@admin.register(AreasTecnologicas)
class AreasTecnologicasAdmin(admin.ModelAdmin):
    list_display = ("id_area_tecnologica", "area_tecnologica")
    search_fields = ("area_tecnologica",)
    ordering = ("area_tecnologica",)

@admin.register(Colaboradores)
class ColaboradoresAdmin(admin.ModelAdmin):
    list_display = ("id_colaborador", "nome", "cpf", "dt_nascimento")
    search_fields = ("nome", "cpf")
    list_filter = ("dt_nascimento",)
    ordering = ("nome",)

class EquipeInline(admin.TabularInline):
    model = Projetos.equipe.through
    extra = 1

@admin.register(Projetos)
class ProjetosAdmin(admin.ModelAdmin):
    list_display = (
        "id_projeto", "projeto", "id_financiador", "id_area_tecnologica",
        "coordenador", "ativo", "inicio_vigencia", "fim_vigencia", "valor", "qtd_membros"
    )
    search_fields = ("projeto", "coordenador", "id_financiador__financiador")
    list_filter = ("ativo", "inicio_vigencia", "fim_vigencia", "id_area_tecnologica")
    ordering = ("inicio_vigencia",)
    inlines = [EquipeInline]