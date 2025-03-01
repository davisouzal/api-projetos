from .models import Financiadores

class FinanciadorRepository:
    @staticmethod
    def get_all():
        return Financiadores.objects.all()

    @staticmethod
    def get_by_id(pk):
        return Financiadores.objects.get(pk=pk)

    @staticmethod
    def filter_by_name(name):
        return Financiadores.objects.filter(financiador__icontains=name)

    @staticmethod
    def create(data):
        return Financiadores.objects.create(**data)

    @staticmethod
    def update(instance, data):
        for attr, value in data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    @staticmethod
    def delete(instance):
        instance.delete()
