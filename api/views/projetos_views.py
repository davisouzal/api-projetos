from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.services.projetos_service import ProjetosService
from api.error_handler import error_handler

@api_view(['GET', 'POST'])
def projetos_list(request):
    try:
        if request.method == 'GET':
            name = request.query_params.get('nome', None)
            projetos = ProjetosService.list_all(name)
            return Response(projetos)
        
        elif request.method == 'POST':
            data = ProjetosService.create(request.data)
            return Response(data, status=status.HTTP_201_CREATED)
        
    except Exception as e:
        errorResponse, status_code = error_handler(e)
        return Response(errorResponse, status=status_code)

@api_view(['GET', 'PUT', 'DELETE'])
def projetos_detail(request, id):
    try:
        projeto = ProjetosService.get_by_id(id)

        if request.method == 'GET':
            return Response(ProjetosService.serialize(projeto), status=status.HTTP_200_OK)
        
        elif request.method == 'PUT':
            data = ProjetosService.update(projeto, request.data)
            return Response(data, status=status.HTTP_200_OK)
        
        elif request.method == 'DELETE':
            ProjetosService.delete(projeto)
            return Response(status=status.HTTP_204_NO_CONTENT)
        
    except Exception as e:
        errorResponse, status_code = error_handler(e)
        return Response(errorResponse, status=status_code)
