from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.services.projetos_service import ProjetosService
from api.error_handler import error_handler
from api.handlers.projetos_handler import format_all_projects, format_team_project
from api.exceptions import ValidationException

@api_view(['GET', 'POST'])
def projetos_list(request):
    try:
        if request.method == 'GET':
            projetos = ProjetosService.list_all()
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
            return Response(format_all_projects(projeto), status=status.HTTP_200_OK)
        
        elif request.method == 'PUT':
            data = ProjetosService.update(projeto, request.data)
            return Response(data, status=status.HTTP_200_OK)
        
        elif request.method == 'DELETE':
            ProjetosService.delete(projeto)
            return Response(status=status.HTTP_204_NO_CONTENT)
        
    except Exception as e:
        errorResponse, status_code = error_handler(e)
        return Response(errorResponse, status=status_code)
    
@api_view(['GET'])
def projetos_info_form(request):
    try:
        data = ProjetosService.get_info_form()
        return Response(data)
    
    except Exception as e:
        errorResponse, status_code = error_handler(e)
        return Response(errorResponse, status=status_code)
    
@api_view(['GET'])
def projetos_listar(request):
    try:
        fields = ['id_projeto', 'projeto', 'ativo', 'inicio_vigencia', 'fim_vigencia']
        projetos = ProjetosService.list_all_selected_fields(fields)
        return Response(projetos)
    
    except Exception as e:
        errorResponse, status_code = error_handler(e)
        return Response(errorResponse, status=status_code)

@api_view(['POST'])
def projetos_create(request):
    try:
        data = ProjetosService.create(request.data)
        return Response(data, status=status.HTTP_201_CREATED)
    
    except Exception as e:
        errorResponse, status_code = error_handler(e)
        return Response(errorResponse, status=status_code)
    
@api_view(['POST'])
def inactivate_project(request, id):
    try:
        projeto = ProjetosService.get_by_id(id)

        data = ProjetosService.change_project_activity(projeto, False)
        return Response(data, status=status.HTTP_200_OK)
    
    except Exception as e:
        errorResponse, status_code = error_handler(e)
        return Response(errorResponse, status=status_code)
    
@api_view(['POST'])
def activate_project(request, id):
    try:
        projeto = ProjetosService.get_by_id(id)

        data = ProjetosService.change_project_activity(projeto, True)
        return Response(data, status=status.HTTP_200_OK)
    
    except Exception as e:
        errorResponse, status_code = error_handler(e)
        return Response(errorResponse, status=status_code)
    
@api_view(['PATCH'])
def edit_project(request, id):
    try:
        projeto = ProjetosService.get_by_id(id)

        data = ProjetosService.update(projeto, request.data)
        return Response(data, status=status.HTTP_200_OK)

    except Exception as e:
        errorResponse, status_code = error_handler(e)
        return Response(errorResponse, status=status_code)
    
@api_view(['GET'])
def view_project(request, id):
    try:
        projeto = ProjetosService.get_by_id(id)

        return Response(format_all_projects(projeto), status=status.HTTP_200_OK)
    
    except Exception as e:
        errorResponse, status_code = error_handler(e)
        return Response(errorResponse, status=status_code)
    
@api_view(['GET'])
def get_team_project(request, id):
    try:
        projeto = ProjetosService.get_by_id(id)

        return Response(format_team_project(projeto), status=status.HTTP_200_OK)
    
    except Exception as e:
        errorResponse, status_code = error_handler(e)
        return Response(errorResponse, status=status_code)
    
@api_view(['PATCH'])
def edit_team_project(request, id):
    try:
        if list(request.data.keys()) != ["equipe"]:
            raise ValidationException("Projeto", "Apenas a equipe pode ser atualizada") 
            
        projeto = ProjetosService.get_by_id(id)

        data = ProjetosService.update(projeto, {"equipe": request.data["equipe"]})
        return Response(data, status=status.HTTP_200_OK)

    except Exception as e:
        errorResponse, status_code = error_handler(e)
        return Response(errorResponse, status=status_code)