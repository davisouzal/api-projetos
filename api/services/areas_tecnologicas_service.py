from django.core.exceptions import ObjectDoesNotExist

from api.repositories.areas_tecnologicas_repository import AreasTecnologicasRepository
from api.serializers.areas_tecnologicas_serializer import AreasTecnologicasSerializer
from api.exceptions import NotFoundException, ValidationException

AreasTecnologicas = 'Áreas Tecnológicas'

class AreasTecnologicasService:
    @staticmethod
    def list_all(area_tecnologica=None):
        if area_tecnologica:
            areas_tecnologicas = AreasTecnologicasRepository.filter_by_area_tecnologica(area_tecnologica)
        else:
            areas_tecnologicas = AreasTecnologicasRepository.get_all()
        return AreasTecnologicasSerializer(areas_tecnologicas, many=True).data

    @staticmethod
    def get_by_id(id):
        try:
            return AreasTecnologicasRepository.get_by_id(id)
        except ObjectDoesNotExist:
            raise NotFoundException(AreasTecnologicas)

    @staticmethod
    def create(data):
        serializer = AreasTecnologicasSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        raise ValidationException(AreasTecnologicas, serializer.errors)

    @staticmethod
    def update(instance, data):
        serializer = AreasTecnologicasSerializer(instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        raise ValidationException(AreasTecnologicas, serializer.errors)

    @staticmethod
    def delete(instance):
        instance.delete()

    @staticmethod
    def serialize(instance):
        return AreasTecnologicasSerializer(instance).data
