from django.core.exceptions import ObjectDoesNotExist

from .repositories import FinanciadorRepository
from .serializers import FinanciadoresSerializer
from .exceptions import NotFoundException, ValidationException

class FinanciadorService:
    @staticmethod
    def list_all(financiador=None):
        if financiador:
            financiadores = FinanciadorRepository.filter_by_name(financiador)
        else:
            financiadores = FinanciadorRepository.get_all()

        serializer = FinanciadoresSerializer(financiadores, many=True)
        
        return serializer.data

    @staticmethod
    def get_by_id(pk):
        try:
            return FinanciadorRepository.get_by_id(pk)
        except ObjectDoesNotExist:
            raise NotFoundException('Financiador')

    @staticmethod
    def create(data):
        serializer = FinanciadoresSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        raise ValidationException('Financiador', serializer.errors)

    @staticmethod
    def update(instance, data):
        serializer = FinanciadoresSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        raise ValidationException('Financiador', serializer.errors)

    @staticmethod
    def delete(instance):
        instance.delete()

    @staticmethod
    def serialize(instance):
        serializer = FinanciadoresSerializer(instance)
        return serializer.data
