from django.urls import path
from api.views.areas_tecnologicas_views import areas_tecnologicas_list, areas_tecnologicas_detail

urlpatterns = [
    path('', areas_tecnologicas_list, name='areas-tecnologicas-list'),
    path('<int:id>/', areas_tecnologicas_detail, name='areas-tecnologicas-detail'),
]
