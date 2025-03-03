from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from api.services.projetos_service import ProjetosService
from api.handlers.error_handler import error_handler
from api.handlers.projetos_handler import format_all_projects, format_team_project
from api.exceptions import ValidationException

@swagger_auto_schema(method='DELETE', responses={204: 'Projeto excluído', 404: 'Projeto não encontrado', 500: 'Erro interno'})
@api_view(['DELETE'])
def delete_project(request, id):
    "Deleta um projeto"
    try:
        projeto = ProjetosService.get_by_id(id)
        ProjetosService.delete(projeto)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    except Exception as e:
        errorResponse, status_code = error_handler(e)
        return Response(errorResponse, status=status_code)

@swagger_auto_schema(method='GET', responses={200: 'Informações do formulário de projetos', 500: 'Erro interno'})
@api_view(['GET'])
def projetos_info_form(request):
    "Retorna informações para o formulário de projetos"
    try:
        data = ProjetosService.get_info_form()
        return Response(data)
    
    except Exception as e:
        errorResponse, status_code = error_handler(e)
        return Response(errorResponse, status=status_code)

@swagger_auto_schema(method='GET', responses={200: 'Lista de projetos', 500: 'Erro interno'})
@api_view(['GET'])
def projetos_listar(request):
    "Lista todos os projetos"
    try:
        fields = ['id_projeto', 'projeto', 'ativo', 'inicio_vigencia', 'fim_vigencia']
        projetos = ProjetosService.list_all_selected_fields(fields)
        return Response(projetos)
    
    except Exception as e:
        errorResponse, status_code = error_handler(e)
        return Response(errorResponse, status=status_code)

@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'projeto': openapi.Schema(type=openapi.TYPE_STRING, description='Nome do projeto'),
        'id_financiador': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID do financiador do projeto'),
        'id_area_tecnologica': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID da área tecnológica do projeto'),
        'coordenador': openapi.Schema(type=openapi.TYPE_STRING, description='Nome do coordenador do projeto'),
        'ativo': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Status ativo do projeto'),
        'inicio_vigencia': openapi.Schema(type=openapi.TYPE_STRING, format='date', description='Data de início da vigência do projeto'),
        'fim_vigencia': openapi.Schema(type=openapi.TYPE_STRING, format='date', description='Data de fim da vigência do projeto'),
        'valor': openapi.Schema(type=openapi.TYPE_NUMBER, format='float', description='Valor do projeto'),
        'equipe': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_INTEGER), description='IDs dos membros da equipe do projeto')
    }
), responses={201: 'Projeto criado', 400: 'Erro de validação', 500: 'Erro interno'})
@api_view(['POST'])
def projetos_create(request):
    "Cria um projeto"
    try:
        data = ProjetosService.create(request.data)
        return Response(data, status=status.HTTP_201_CREATED)
    
    except Exception as e:
        errorResponse, status_code = error_handler(e)
        return Response(errorResponse, status=status_code)

@swagger_auto_schema(method='POST', responses={200: 'Projeto inativado', 404: 'Projeto não encontrado', 500: 'Erro interno'})
@api_view(['POST'])
def inactivate_project(request, id):
    "Muda o status de um projeto para inativo"
    try:
        projeto = ProjetosService.get_by_id(id)

        data = ProjetosService.change_project_activity(projeto, False)
        return Response(data, status=status.HTTP_200_OK)
    
    except Exception as e:
        errorResponse, status_code = error_handler(e)
        return Response(errorResponse, status=status_code)

@swagger_auto_schema(method='POST', responses={200: 'Projeto ativado', 404: 'Projeto não encontrado', 500: 'Erro interno'})
@api_view(['POST'])
def activate_project(request, id):
    "Muda o status de um projeto para ativo"
    try:
        projeto = ProjetosService.get_by_id(id)

        data = ProjetosService.change_project_activity(projeto, True)
        return Response(data, status=status.HTTP_200_OK)
    
    except Exception as e:
        errorResponse, status_code = error_handler(e)
        return Response(errorResponse, status=status_code)

@swagger_auto_schema(method='PATCH', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    anyOf=[
        {'projeto': openapi.Schema(type=openapi.TYPE_STRING)},
        {'id_financiador': openapi.Schema(type=openapi.TYPE_INTEGER)},
        {'id_area_tecnologica': openapi.Schema(type=openapi.TYPE_INTEGER)},
        {'coordenador': openapi.Schema(type=openapi.TYPE_STRING)},
        {'ativo': openapi.Schema(type=openapi.TYPE_BOOLEAN)},
        {'inicio_vigencia': openapi.Schema(type=openapi.TYPE_STRING, format='date')},
        {'fim_vigencia': openapi.Schema(type=openapi.TYPE_STRING, format='date')},
        {'valor': openapi.Schema(type=openapi.TYPE_NUMBER, format='float')},
        {'qtd_membros': openapi.Schema(type=openapi.TYPE_INTEGER)},
        {'equipe': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_INTEGER))}
    ],
    properties={
        'projeto': openapi.Schema(type=openapi.TYPE_STRING),
        'id_financiador': openapi.Schema(type=openapi.TYPE_INTEGER),
        'id_area_tecnologica': openapi.Schema(type=openapi.TYPE_INTEGER),
        'coordenador': openapi.Schema(type=openapi.TYPE_STRING),
        'ativo': openapi.Schema(type=openapi.TYPE_BOOLEAN),
        'inicio_vigencia': openapi.Schema(type=openapi.TYPE_STRING, format='date'),
        'fim_vigencia': openapi.Schema(type=openapi.TYPE_STRING, format='date'),
        'valor': openapi.Schema(type=openapi.TYPE_NUMBER, format='float'),
        'qtd_membros': openapi.Schema(type=openapi.TYPE_INTEGER),
        'equipe': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_INTEGER))
    }
), responses={200: 'Projeto atualizado', 400: 'Erro de validação', 404: 'Projeto não encontrado', 500: 'Erro interno'})
@api_view(['PATCH'])
def edit_project(request, id):
    try:
        projeto = ProjetosService.get_by_id(id)

        data = ProjetosService.update(projeto, request.data)
        return Response(data, status=status.HTTP_200_OK)

    except Exception as e:
        errorResponse, status_code = error_handler(e)
        return Response(errorResponse, status=status_code)

@swagger_auto_schema(method='GET', responses={200: 'Projeto encontrado', 404: 'Projeto não encontrado', 500: 'Erro interno'})
@api_view(['GET'])
def view_project(request, id):
    "Visualiza um projeto com informações mais detalhadas"
    try:
        projeto = ProjetosService.get_by_id(id)

        return Response(format_all_projects(projeto), status=status.HTTP_200_OK)
    
    except Exception as e:
        errorResponse, status_code = error_handler(e)
        return Response(errorResponse, status=status_code)

@swagger_auto_schema(method='GET', responses={200: 'Equipe do projeto encontrada', 404: 'Projeto não encontrado', 500: 'Erro interno'})
@api_view(['GET'])
def get_team_project(request, id):
    "Visualiza a equipe de um projeto"
    try:
        projeto = ProjetosService.get_by_id(id)

        return Response(format_team_project(projeto), status=status.HTTP_200_OK)
    
    except Exception as e:
        errorResponse, status_code = error_handler(e)
        return Response(errorResponse, status=status_code)

@swagger_auto_schema(method='PATCH', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'equipe': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_INTEGER))
    }
), responses={200: 'Equipe do projeto atualizada', 400: 'Erro de validação',404: 'Projeto não encontrado', 500: 'Erro interno'})
@api_view(['PATCH'])
def edit_team_project(request, id):
    "Atualiza a equipe de um projeto"
    try:
        if list(request.data.keys()) != ["equipe"]:
            raise ValidationException("Projeto", "Apenas a equipe pode ser atualizada") 
            
        projeto = ProjetosService.get_by_id(id)

        data = ProjetosService.update(projeto, {"equipe": request.data["equipe"]})
        return Response(data, status=status.HTTP_200_OK)

    except Exception as e:
        errorResponse, status_code = error_handler(e)
        return Response(errorResponse, status=status_code)