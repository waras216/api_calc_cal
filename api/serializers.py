from rest_framework import serializers
from .models import Alimento, RegistroComida

class AlimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alimento
        fields = '__all__'

class RegistroComidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroComida
        fields = '__all__'
