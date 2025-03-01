from api.models.areas_tecnologicas import AreasTecnologicas

class AreasTecnologicasRepository:
    @staticmethod
    def get_all():
        return AreasTecnologicas.objects.all()

    @staticmethod
    def get_by_id(id):
        return AreasTecnologicas.objects.get(pk=id)

    @staticmethod
    def filter_by_area_tecnologica(area_tecnologica):
        return AreasTecnologicas.objects.filter(area_tecnologica__contains=area_tecnologica)

    @staticmethod
    def create(data):
        return AreasTecnologicas.objects.create(**data)

    @staticmethod
    def update(instance, data):
        for attr, value in data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    @staticmethod
    def delete(instance):
        instance.delete()
