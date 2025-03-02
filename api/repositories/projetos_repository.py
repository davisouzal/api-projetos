from api.models import Projetos

class ProjetosRepository:
    @staticmethod
    def get_all(fields=None):
        return Projetos.objects.values(*fields) if fields else Projetos.objects.all()

    @staticmethod
    def get_by_id(id):
        return Projetos.objects.select_related(
            'id_area_tecnologica', 'id_financiador'
        ).prefetch_related(
            'equipe'
        ).get(pk=id)

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
