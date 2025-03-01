from rest_framework import serializers
from api.models.colaboradores import Colaboradores

class ColaboradoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colaboradores
        fields = '__all__'