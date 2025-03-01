from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.services.financiadores_service import FinanciadoresService
from api.error_handler import error_handler

@api_view(['GET', 'POST'])
def financiadores_list(request):
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

@api_view(['GET', 'PUT', 'DELETE'])
def financiadores_detail(request, pk):
    try:
        financiador = FinanciadoresService.get_by_id(pk)

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
