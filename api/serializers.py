from rest_framework import serializers
from .models import Financiadores, AreasTecnologicas, Colaboradores, Projetos

class FinanciadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Financiadores
        fields = '__all__'

class AreasTecnologicasSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreasTecnologicas
        fields = '__all__'

class ColaboradoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colaboradores
        fields = '__all__'

class ProjetosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projetos
        fields = '__all__'
