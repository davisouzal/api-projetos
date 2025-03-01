from rest_framework import serializers
from api.models.projetos import Projetos

class ProjetosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projetos
        fields = '__all__'
