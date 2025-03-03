from django.urls import path
from api.views.projetos_views import (
    delete_project, projetos_info_form, projetos_listar, projetos_create,
    inactivate_project, activate_project, edit_project, view_project, 
    get_team_project, edit_team_project
)

urlpatterns = [
    path('<int:id>/excluir', delete_project, name='projetos-detail'),
    path('form/', projetos_info_form, name='projetos-info-form'),
    path('listar/', projetos_listar, name='projetos-listar'),
    path('cadastrar/', projetos_create, name='projetos-create'),
    path('<int:id>/inativar/', inactivate_project, name='inactivate-project'),
    path('<int:id>/ativar/', activate_project, name='activate-project'),
    path('<int:id>/editar/', edit_project, name='editar-projeto'),
    path('<int:id>/visualizar/', view_project, name='visualizar-projeto'),
    path('<int:id>/equipe/', get_team_project, name='visualizar-equipe-projeto'),
    path('<int:id>/equipe/atualizar/', edit_team_project, name='atualizar-equipe-projeto'),
]
