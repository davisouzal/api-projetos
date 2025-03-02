from django.urls import path

from api.views.financiadores_views import financiadores_list, financiadores_detail
from api.views.colaboradores_views import colaboradores_list, colaboradores_detail, colaboradores_listar, colaboradores_create, colaboradores_edit, colaboradores_view
from api.views.areas_tecnologicas_views import areas_tecnologicas_list, areas_tecnologicas_detail
from api.views.projetos_views import projetos_list, projetos_detail, projetos_info_form, projetos_listar, projetos_create, inactivate_project, activate_project, edit_project, view_project, get_team_project, edit_team_project

urlpatterns = [
    path('financiadores/', financiadores_list, name='financiadores-list'),
    path('financiadores/<int:id>/', financiadores_detail, name='financiadores-detail'),

    path('colaboradores/', colaboradores_list, name='colaboradores-list'),
    path('colaboradores/<int:id>/', colaboradores_detail, name='colaboradores-detail'),
    path('colaboradores/listar/', colaboradores_listar, name='colaboradores_listar'),
    path('colaboradores/cadastrar/', colaboradores_create, name='colaboradores-create'),
    path('colaboradores/<int:id>/editar/', colaboradores_edit, name='colaboradores-edit'),
    path('colaboradores/<int:id>/visualizar/', colaboradores_view, name='colaboradores-view'),

    path('areas-tecnologicas/', areas_tecnologicas_list, name='areas-tecnologicas-list'),
    path('areas-tecnologicas/<int:id>/', areas_tecnologicas_detail, name='areas-tecnologicas-detail'),

    path('projetos/', projetos_list, name='projetos-list'),
    path('projetos/<int:id>/', projetos_detail, name='projetos-detail'),
    
    path('projetos/form/', projetos_info_form, name='projetos-info-form'),
    path('projetos/listar/', projetos_listar, name='projetos-listar'),
    path('projetos/cadastrar/', projetos_create, name='projetos-create'),
    path('projetos/<int:id>/inativar/', inactivate_project, name='inactivate-project'),
    path('projetos/<int:id>/ativar/', activate_project, name='activate-project'),
    path('projetos/<int:id>/editar/', edit_project, name='editar-projeto'),
    path('projetos/<int:id>/visualizar/', view_project, name='visualizar-projeto'),
    path('projetos/<int:id>/equipe/', get_team_project, name='visualizar-equipe-projeto'),
    path('projetos/<int:id>/equipe/atualizar/', edit_team_project, name='atualizar-equipe-projeto'),
]
