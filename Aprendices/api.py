from .serializers import AprendizSerializer, UsoComputadorSerializer
from .models import Aprendiz, Uso_computador
from rest_framework import viewsets
from Computadores.serializers import ComputadorSerializer
from django.contrib.auth.models import User

class AprendizViewSet(viewsets.ModelViewSet):
    queryset = Aprendiz.objects.all()
    serializer_class = AprendizSerializer

class UsoComputadorViewSet(viewsets.ModelViewSet):
    queryset = Uso_computador.objects.all()
    serializer_class = UsoComputadorSerializer
