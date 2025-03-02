from django.core.exceptions import ObjectDoesNotExist

from api.repositories.projetos_repository import ProjetosRepository
from api.repositories.colaboradores_repository import ColaboradoresRepository
from api.repositories.areas_tecnologicas_repository import AreasTecnologicasRepository
from api.repositories.financiadores_repository import FinanciadoresRepository
from api.serializers.projetos_serializer import ProjetosSerializer
from api.exceptions import NotFoundException, ValidationException

Projetos = 'Projeto'

class ProjetosService:
    @staticmethod
    def list_all():
        projetos = ProjetosRepository.get_all()
        return ProjetosSerializer(projetos, many=True).data
    
    def list_all_selected_fields(fields):
        projetos = ProjetosRepository.get_all(fields)
        return projetos

    @staticmethod
    def get_by_id(id):
        try:
            return ProjetosRepository.get_by_id(id)
        except ObjectDoesNotExist:
            raise NotFoundException(Projetos)

    @staticmethod
    def create(data):
        data['qtd_membros'] = len(data.get('equipe', []))
        serializer = ProjetosSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        raise ValidationException(Projetos, serializer.errors)

    @staticmethod
    def update(instance, data):
        if 'equipe' in data:
            data['qtd_membros'] = len(data.get('equipe', []))
        serializer = ProjetosSerializer(instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        raise ValidationException(Projetos, serializer.errors)
    
    @staticmethod
    def change_project_activity(instance, activity):
        instance.ativo = activity
        instance.save()
        return ProjetosSerializer(instance).data

    @staticmethod
    def delete(instance):
        instance.delete()
    
    @staticmethod
    def get_info_form():
        colaboradores_fields = ['id_colaborador', 'nome']
        colaboaradores = ColaboradoresRepository.get_all(colaboradores_fields)

        areas_tecnologicas_fields = ['id_area_tecnologica', 'area_tecnologica']
        areas_tecnologicas = AreasTecnologicasRepository.get_all(areas_tecnologicas_fields)
        
        financiadores_fields = ['id_financiador', 'financiador']
        financiadores = FinanciadoresRepository.get_all(financiadores_fields)

        return {
            'colaboradores': colaboaradores,
            'areas_tecnologicas': areas_tecnologicas,
            'financiadores': financiadores
        }


