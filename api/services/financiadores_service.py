from django.core.exceptions import ObjectDoesNotExist

from api.repositories.financiadores_repository import FinanciadoresRepository
from api.serializers.financiadores_serializer import FinanciadoresSerializer
from api.exceptions import NotFoundException, ValidationException

Financiadores = 'Financiador'

class FinanciadoresService:
    @staticmethod
    def list_all(financiador=None):
        if financiador:
            financiadores = FinanciadoresRepository.filter_by_financiador(financiador)
        else:
            financiadores = FinanciadoresRepository.get_all()
        return FinanciadoresSerializer(financiadores, many=True).data

    @staticmethod
    def get_by_id(id):
        try:
            return FinanciadoresRepository.get_by_id(id)
        except ObjectDoesNotExist:
            raise NotFoundException(Financiadores)

    @staticmethod
    def create(data):
        serializer = FinanciadoresSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        raise ValidationException(Financiadores, serializer.errors)

    @staticmethod
    def update(instance, data):
        serializer = FinanciadoresSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        raise ValidationException(Financiadores, serializer.errors)

    @staticmethod
    def delete(instance):
        instance.delete()

    @staticmethod
    def serialize(instance):
        return FinanciadoresSerializer(instance).data
