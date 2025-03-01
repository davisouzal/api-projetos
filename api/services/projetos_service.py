from django.core.exceptions import ObjectDoesNotExist

from api.repositories.projetos_repository import ProjetosRepository
from api.serializers.projetos_serializer import ProjetosSerializer
from api.exceptions import NotFoundException, ValidationException

Projetos = 'Projeto'

class ProjetosService:
    @staticmethod
    def list_all(name=None):
        if name:
            projetos = ProjetosRepository.filter_by_name(name)
        else:
            projetos = ProjetosRepository.get_all()
        return ProjetosSerializer(projetos, many=True).data

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
        data['qtd_membros'] = len(data.get('equipe', []))
        serializer = ProjetosSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        raise ValidationException(Projetos, serializer.errors)

    @staticmethod
    def delete(instance):
        instance.delete()

    @staticmethod
    def serialize(instance):
        return ProjetosSerializer(instance).data
