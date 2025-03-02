from django.urls import path, include

urlpatterns = [
    path('financiadores/', include('api.urls.financiadores_urls')),
    path('colaboradores/', include('api.urls.colaboradores_urls')),
    path('areas-tecnologicas/', include('api.urls.areas_tecnologicas_urls')),
    path('projetos/', include('api.urls.projetos_urls')),
]
