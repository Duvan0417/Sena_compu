from .models import Aprendiz, Uso_computador
from rest_framework import serializers
from django.contrib.auth.models import User

class AprendizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aprendiz
        fields = '__all__'

class UsoComputadorSerializer(serializers.ModelSerializer):
    Aprendiz_info = serializers.StringRelatedField(source='ID_aprendiz', read_only=True)
    Computador_info = serializers.StringRelatedField(source='ID_computador', read_only=True)
    User_info = serializers.StringRelatedField(source='ID_User', read_only=True)
    class Meta:
        model = Uso_computador
        fields = '__all__'