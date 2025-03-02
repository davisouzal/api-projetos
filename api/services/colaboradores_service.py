from django.core.exceptions import ObjectDoesNotExist

from api.repositories.colaboradores_repository import ColaboradoresRepository
from api.serializers.colaboradores_serializer import ColaboradoresSerializer
from api.exceptions import NotFoundException, ValidationException

Colaboradores = 'Colaborador'

class ColaboradoresService:
    @staticmethod
    def list_all(name=None):
        if name:
            colaboradores = ColaboradoresRepository.filter_by_name(name)
        else:
            colaboradores = ColaboradoresRepository.get_all()
        return ColaboradoresSerializer(colaboradores, many=True).data
    
    def list_all_selected_fields(fields):
        colaboradores = ColaboradoresRepository.get_all(fields)
        return colaboradores

    @staticmethod
    def get_by_id(id):
        try:
            return ColaboradoresRepository.get_by_id(id)
        except ObjectDoesNotExist:
            raise NotFoundException(Colaboradores)

    @staticmethod
    def create(data):
        serializer = ColaboradoresSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        raise ValidationException(Colaboradores, serializer.errors)

    @staticmethod
    def update(instance, data):
        serializer = ColaboradoresSerializer(instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        raise ValidationException(Colaboradores, serializer.errors)

    @staticmethod
    def delete(instance):
        instance.delete()

    @staticmethod
    def serialize(instance):
        return ColaboradoresSerializer(instance).data
