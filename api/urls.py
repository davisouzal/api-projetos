from django.urls import path

from api.views.financiadores_views import financiadores_list, financiadores_detail
from api.views.colaboradores_views import colaboradores_list, colaboradores_detail
from api.views.areas_tecnologicas_views import areas_tecnologicas_list, areas_tecnologicas_detail
from api.views.projetos_views import projetos_list, projetos_detail

urlpatterns = [
    path('financiadores/', financiadores_list, name='financiadores-list'),
    path('financiadores/<int:id>/', financiadores_detail, name='financiadores-detail'),

    path('colaboradores/', colaboradores_list, name='colaboradores-list'),
    path('colaboradores/<int:id>/', colaboradores_detail, name='colaboradores-detail'),

    path('areas-tecnologicas/', areas_tecnologicas_list, name='areas-tecnologicas-list'),
    path('areas-tecnologicas/<int:id>/', areas_tecnologicas_detail, name='areas-tecnologicas-detail'),

    path('projetos/', projetos_list, name='projetos-list'),
    path('projetos/<int:id>/', projetos_detail, name='projetos-detail'),
]
