from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from api.services.colaboradores_service import ColaboradoresService
from api.handlers.error_handler import error_handler

@swagger_auto_schema(method='GET', responses={200: 'Lista de colaboradores', 500: 'Erro interno'})
@swagger_auto_schema(method='POST', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'cpf': openapi.Schema(type=openapi.TYPE_STRING, description='CPF do colaborador'),
        'nome': openapi.Schema(type=openapi.TYPE_STRING, description='Nome do colaborador'),
        'dt_nascimento': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE, description='Data de nascimento do colaborador')
    }
), responses={201: 'Colaborador criado', 400: 'Erro de validação', 500: 'Erro interno'})
@api_view(['GET', 'POST'])
def colaboradores_list(request):
    try:
        if request.method == 'GET':
            name = request.query_params.get('nome', None)
            colaboradores = ColaboradoresService.list_all(name)
            return Response(colaboradores)
        
        elif request.method == 'POST':
            data = ColaboradoresService.create(request.data)
            return Response(data, status=status.HTTP_201_CREATED)
        
    except Exception as e:
        errorResponse, status_code = error_handler(e)
        return Response(errorResponse, status=status_code)

@swagger_auto_schema(method='GET', responses={200: 'Detalhes do colaborador', 404: 'Colaborador não encontrado', 500: 'Erro interno'})
@swagger_auto_schema(method='PUT', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'cpf': openapi.Schema(type=openapi.TYPE_STRING, description='CPF do colaborador'),
        'nome': openapi.Schema(type=openapi.TYPE_STRING, description='Nome do colaborador'),
        'dt_nascimento': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE, description='Data de nascimento do colaborador')
    }
), responses={200: 'Colaborador atualizado', 404: 'Colaborador não encontrado', 500: 'Erro interno'})
@swagger_auto_schema(method='DELETE', responses={204: 'Colaborador deletado', 404: 'Colaborador não encontrado', 500: 'Erro interno'})
@api_view(['GET', 'PUT', 'DELETE'])
def colaboradores_detail(request, id):
    try:
        colaborador = ColaboradoresService.get_by_id(id)

        if request.method == 'GET':
            return Response(ColaboradoresService.serialize(colaborador), status=status.HTTP_200_OK)
        
        elif request.method == 'PUT':
            data = ColaboradoresService.update(colaborador, request.data)
            return Response(data, status=status.HTTP_200_OK)
        
        elif request.method == 'DELETE':
            ColaboradoresService.delete(colaborador)
            return Response(status=status.HTTP_204_NO_CONTENT)
        
    except Exception as e:
        errorResponse, status_code = error_handler(e)
        return Response(errorResponse, status=status_code)

@swagger_auto_schema(method='GET', responses={200: 'Lista de colaboradores', 500: 'Erro interno'})
@api_view(['GET'])
def colaboradores_listar(request):
    "Listar colaboradores"
    try:
        fields = ['id_colaborador', 'nome']
        colaboradores = ColaboradoresService.list_all_selected_fields(fields)
        return Response(colaboradores)
    
    except Exception as e:
        errorResponse, status_code = error_handler(e)
        return Response(errorResponse, status=status_code)

@swagger_auto_schema(method='POST', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'cpf': openapi.Schema(type=openapi.TYPE_STRING, description='CPF do colaborador'),
        'nome': openapi.Schema(type=openapi.TYPE_STRING, description='Nome do colaborador'),
        'dt_nascimento': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE, description='Data de nascimento do colaborador')
    }
))
@api_view(['POST'])
def colaboradores_create(request):
    "Criar colaborador"
    try:
        data = ColaboradoresService.create(request.data)
        return Response(data, status=status.HTTP_201_CREATED)
    
    except Exception as e:
        errorResponse, status_code = error_handler(e)
        return Response(errorResponse, status=status_code)

@swagger_auto_schema(method='GET', responses={200: 'Detalhes do colaborador', 404: 'Colaborador não encontrado', 500: 'Erro interno'})    
@api_view(['GET'])
def colaboradores_view(request, id):
    "Detalhes do colaborador"
    try:
        colaborador = ColaboradoresService.get_by_id(id)
        return Response(ColaboradoresService.serialize(colaborador), status=status.HTTP_200_OK)
    
    except Exception as e:
        errorResponse, status_code = error_handler(e)
        return Response(errorResponse, status=status_code)

@swagger_auto_schema(method='PATCH', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'cpf': openapi.Schema(type=openapi.TYPE_STRING, description='CPF do colaborador'),
        'nome': openapi.Schema(type=openapi.TYPE_STRING, description='Nome do colaborador'),
        'dt_nascimento': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE, description='Data de nascimento do colaborador')
    }
), responses={200: 'Colaborador atualizado', 404: 'Colaborador não encontrado', 500: 'Erro interno'})   
@api_view(['PATCH'])
def colaboradores_edit(request, id):
    "Editar colaborador"
    try:
        colaborador = ColaboradoresService.get_by_id(id)
        data = ColaboradoresService.update(colaborador, request.data)
        return Response(data, status=status.HTTP_200_OK)
    
    except Exception as e:
        errorResponse, status_code = error_handler(e)
        return Response(errorResponse, status=status_code)
