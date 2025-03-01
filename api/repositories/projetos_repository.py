from api.models import Projetos

class ProjetosRepository:
    @staticmethod
    def get_all():
        return Projetos.objects.all()

    @staticmethod
    def get_by_id(id):
        return Projetos.objects.get(pk=id)

    @staticmethod
    def filter_by_name(name):
        return Projetos.objects.filter(nome__icontains=name)

    @staticmethod
    def create(data):
        return Projetos.objects.create(**data)

    @staticmethod
    def update(instance, data):
        for attr, value in data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    @staticmethod
    def delete(instance):
        instance.delete()
