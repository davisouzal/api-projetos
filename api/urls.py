from django.urls import path

from .views import financiadores_list, financiadores_detail

urlpatterns = [
    path('financiadores/', financiadores_list, name='financiadores_list'),
    path('financiadores/<int:pk>/', financiadores_detail),
]