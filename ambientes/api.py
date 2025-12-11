from ambientes.models import Ambiente
from ambientes.serializers import AmbienteSerializer
from rest_framework import viewsets, permissions

class AmbienteViewSet(viewsets.ModelViewSet):
    queryset = Ambiente.objects.all()
    serializer_class = [permissions.AllowAny]
    serializer_class = AmbienteSerializer