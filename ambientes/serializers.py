from rest_framework import serializers
from .models import Ambiente

class AmbienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ambiente
        fields = ['id', 'nombre_ambiente', 'ubicacion', 'capacidad', 'ID_user']
        read_only_fields = ['ID_user']

    def create(self, validated_data):
        validated_data['ID_user'] = self.context['request'].user
        return super().create(validated_data)