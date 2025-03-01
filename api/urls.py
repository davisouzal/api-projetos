from django.urls import path

from api.views.financiadores_views import financiadores_list, financiadores_detail

urlpatterns = [
    path('financiadores/', financiadores_list, name='financiadores-list'),
    path('financiadores/<int:id>/', financiadores_detail, name='financiadores-detail'),
]
