from rest_framework import viewsets
from .models import Computador, Compu_dañados, Mantenimiento, Historial_Ambiente
from .serializers import (
    ComputadorSerializer, 
    ComputadoresDañadosSerializer, 
    MantenimientoSerializer, 
    HistorialAmbienteSerializer)

class ComputadorViewSet(viewsets.ModelViewSet):
    queryset = Computador.objects.all()
    serializer_class = ComputadorSerializer

class ComputadoresDañadosViewSet(viewsets.ModelViewSet):
    queryset = Compu_dañados.objects.all()
    serializer_class = ComputadoresDañadosSerializer

class MantenimientoViewSet(viewsets.ModelViewSet):
    queryset = Mantenimiento.objects.all()
    serializer_class = MantenimientoSerializer

class HistorialAmbienteViewSet(viewsets.ModelViewSet):
    queryset = Historial_Ambiente.objects.all()
    serializer_class = HistorialAmbienteSerializer