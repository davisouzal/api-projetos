from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from api.services.areas_tecnologicas_service import AreasTecnologicasService
from api.handlers.error_handler import error_handler

@swagger_auto_schema(method='GET', responses={200: 'Lista de áreas tecnológicas', 500: 'Erro interno'})
@swagger_auto_schema(method='POST', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'area_tecnologica': openapi.Schema(type=openapi.TYPE_STRING, description='Nome da área tecnológica')
    }
), responses={201: 'Área tecnológica criada', 400: 'Erro de validação', 500: 'Erro interno'})
@api_view(['GET', 'POST'])
def areas_tecnologicas_list(request):
    "Listar ou criar áreas tecnológicas"
    try:
        if request.method == 'GET':
            area_tecnologica = request.query_params.get('area_tecnologica', None)
            area_tecnologica = AreasTecnologicasService.list_all(area_tecnologica)
            return Response(area_tecnologica)
        
        elif request.method == 'POST':
            data = AreasTecnologicasService.create(request.data)
            return Response(data, status=status.HTTP_201_CREATED)
        
    except Exception as e:
        errorResponse, status_code = error_handler(e)
        return Response(errorResponse, status=status_code)

@swagger_auto_schema(method='GET', responses={200: 'Detalhes da área tecnológica', 404: 'Área tecnológica não encontrada', 500: 'Erro interno'})
@swagger_auto_schema(method='PUT', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'area_tecnologica': openapi.Schema(type=openapi.TYPE_STRING, description='Nome da área tecnológica')
    }
), responses={200: 'Área tecnológica atualizada', 404: 'Área tecnológica não encontrada', 500: 'Erro interno'})
@swagger_auto_schema(method='DELETE', responses={204: 'Área tecnológica deletada', 404: 'Área tecnológica não encontrada', 500: 'Erro interno'})
@api_view(['GET', 'PUT', 'DELETE'])
def areas_tecnologicas_detail(request, id):
    "Detalhar, atualizar ou deletar área tecnológica"
    try:
        area_tecnologica = AreasTecnologicasService.get_by_id(id)

        if request.method == 'GET':
            return Response(AreasTecnologicasService.serialize(area_tecnologica), status=status.HTTP_200_OK)
        
        elif request.method == 'PUT':
            data = AreasTecnologicasService.update(area_tecnologica, request.data)
            return Response(data, status=status.HTTP_200_OK)
        
        elif request.method == 'DELETE':
            AreasTecnologicasService.delete(area_tecnologica)
            return Response(status=status.HTTP_204_NO_CONTENT)
        
    except Exception as e:
        errorResponse, status_code = error_handler(e)
        return Response(errorResponse, status=status_code)
