from django.urls import path
from api.views.colaboradores_views import (
    colaboradores_list, colaboradores_detail, colaboradores_listar, 
    colaboradores_create, colaboradores_edit, colaboradores_view
)

urlpatterns = [
    path('', colaboradores_list, name='colaboradores-list'),
    path('<int:id>/', colaboradores_detail, name='colaboradores-detail'),
    path('listar/', colaboradores_listar, name='colaboradores_listar'),
    path('cadastrar/', colaboradores_create, name='colaboradores-create'),
    path('<int:id>/editar/', colaboradores_edit, name='colaboradores-edit'),
    path('<int:id>/visualizar/', colaboradores_view, name='colaboradores-view'),
]
