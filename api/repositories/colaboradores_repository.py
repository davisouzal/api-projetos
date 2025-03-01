from api.models import Colaboradores

class ColaboradoresRepository:
    @staticmethod
    def get_all():
        return Colaboradores.objects.all()

    @staticmethod
    def get_by_id(id):
        return Colaboradores.objects.get(pk=id)

    @staticmethod
    def filter_by_name(name):
        return Colaboradores.objects.filter(nome__icontains=name)

    @staticmethod
    def create(data):
        return Colaboradores.objects.create(**data)

    @staticmethod
    def update(instance, data):
        for attr, value in data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    @staticmethod
    def delete(instance):
        instance.delete()
