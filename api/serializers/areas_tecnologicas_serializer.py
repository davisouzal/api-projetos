from rest_framework import serializers
from api.models.areas_tecnologicas import AreasTecnologicas

class AreasTecnologicasSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreasTecnologicas
        fields = '__all__'