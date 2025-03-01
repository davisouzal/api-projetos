from api.models.financiadores import Financiadores

class FinanciadoresRepository:
    @staticmethod
    def get_all():
        return Financiadores.objects.all()

    @staticmethod
    def get_by_id(id):
        return Financiadores.objects.get(pk=id)

    @staticmethod
    def filter_by_financiador(financiador):
        return Financiadores.objects.filter(financiador__icontains=financiador)

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
