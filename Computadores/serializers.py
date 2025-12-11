from .models import Computador, Compu_dañados, Mantenimiento, Historial_Ambiente
from rest_framework import serializers
from django.contrib.auth.models import User 
from ambientes.models import Ambiente

class ComputadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computador
        fields = '__all__'

class ComputadoresDañadosSerializer(serializers.ModelSerializer):
    compu_informacion = serializers.StringRelatedField(source='ID_computador', read_only=True)
    class Meta:
        model = Compu_dañados
        fields = '__all__'

class MantenimientoSerializer(serializers.ModelSerializer):
    compu_informacion = serializers.StringRelatedField(source='ID_computador', read_only=True)

    class Meta:
        model = Mantenimiento
        fields = '__all__'

class HistorialAmbienteSerializer(serializers.ModelSerializer):
    compu_informacion = serializers.StringRelatedField(source='ID_computador', read_only=True)
    ambiente_informacion = serializers.StringRelatedField(source='ID_ambiente', read_only=True)
    user_informacion = serializers.StringRelatedField(source='ID_user', read_only=True)
    class Meta:
        model = Historial_Ambiente
        fields = '__all__'

