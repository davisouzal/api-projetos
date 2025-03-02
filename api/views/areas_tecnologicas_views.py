from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.services.areas_tecnologicas_service import AreasTecnologicasService
from api.handlers.error_handler import error_handler

@api_view(['GET', 'POST'])
def areas_tecnologicas_list(request):
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

@api_view(['GET', 'PUT', 'DELETE'])
def areas_tecnologicas_detail(request, id):
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
