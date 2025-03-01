from rest_framework import serializers
from api.models.financiadores import Financiadores

class FinanciadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Financiadores
        fields = '__all__'