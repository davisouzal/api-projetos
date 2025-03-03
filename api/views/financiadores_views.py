from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from api.services.financiadores_service import FinanciadoresService
from api.handlers.error_handler import error_handler

@swagger_auto_schema(method='GET', responses={200: 'Lista de financiadores', 500: 'Erro interno'})
@swagger_auto_schema(method='POST', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'financiador': openapi.Schema(type=openapi.TYPE_STRING, description='Nome do financiador')
    }
), responses={201: 'Financiador criado', 400: 'Erro de validação',500: 'Erro interno'})
@api_view(['GET', 'POST'])
def financiadores_list(request):
    "Listar ou criar financiadores"
    try:
        if request.method == 'GET':
            financiador = request.query_params.get('financiador', None)
            financiadores = FinanciadoresService.list_all(financiador)
            return Response(financiadores)
        
        elif request.method == 'POST':
            data = FinanciadoresService.create(request.data)
            return Response(data, status=status.HTTP_201_CREATED)
        
    except Exception as e:
        errorResponse, status_code = error_handler(e)
        return Response(errorResponse, status=status_code)

@swagger_auto_schema(method='GET', responses={200: 'Detalhes do financiador', 404: 'Financiador não encontrado', 500: 'Erro interno'})
@swagger_auto_schema(method='PUT', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'financiador': openapi.Schema(type=openapi.TYPE_STRING, description='Nome do financiador')
    }
), responses={200: 'Financiador atualizado', 404: 'Financiador não encontrado', 500: 'Erro interno'})
@swagger_auto_schema(method='DELETE', responses={204: 'Financiador deletado', 404: 'Financiador não encontrado', 500: 'Erro interno'})
@api_view(['GET', 'PUT', 'DELETE'])
def financiadores_detail(request, id):
    "Detalhar, atualizar ou deletar financiador"
    try:
        financiador = FinanciadoresService.get_by_id(id)

        if request.method == 'GET':
            return Response(FinanciadoresService.serialize(financiador), status=status.HTTP_200_OK)
        
        elif request.method == 'PUT':
            data = FinanciadoresService.update(financiador, request.data)
            return Response(data, status=status.HTTP_200_OK)
        
        elif request.method == 'DELETE':
            FinanciadoresService.delete(financiador)
            return Response(status=status.HTTP_204_NO_CONTENT)
        
    except Exception as e:
        errorResponse, status_code = error_handler(e)
        return Response(errorResponse, status=status_code)
