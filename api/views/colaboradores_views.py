from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.services.colaboradores_service import ColaboradoresService
from api.error_handler import error_handler

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
    
@api_view(['GET'])
def colaboradores_listar(request):
    try:
        fields = ['id_colaborador', 'nome']
        colaboradores = ColaboradoresService.list_all_selected_fields(fields)
        return Response(colaboradores)
    
    except Exception as e:
        errorResponse, status_code = error_handler(e)
        return Response(errorResponse, status=status_code)
    
@api_view(['POST'])
def colaboradores_create(request):
    try:
        data = ColaboradoresService.create(request.data)
        return Response(data, status=status.HTTP_201_CREATED)
    
    except Exception as e:
        errorResponse, status_code = error_handler(e)
        return Response(errorResponse, status=status_code)
    
@api_view(['GET'])
def colaboradores_view(request, id):
    try:
        colaborador = ColaboradoresService.get_by_id(id)
        return Response(ColaboradoresService.serialize(colaborador), status=status.HTTP_200_OK)
    
    except Exception as e:
        errorResponse, status_code = error_handler(e)
        return Response(errorResponse, status=status_code)
    
@api_view(['PATCH'])
def colaboradores_edit(request, id):
    try:
        colaborador = ColaboradoresService.get_by_id(id)
        data = ColaboradoresService.update(colaborador, request.data)
        return Response(data, status=status.HTTP_200_OK)
    
    except Exception as e:
        errorResponse, status_code = error_handler(e)
        return Response(errorResponse, status=status_code)
