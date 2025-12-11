from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import (
    ComputadorViewSet,
    ComputadoresDañadosViewSet,
    MantenimientoViewSet,
    HistorialAmbienteViewSet
)

router = DefaultRouter()
router.register(r'computadores', ComputadorViewSet)
router.register(r'computadores_dañados', ComputadoresDañadosViewSet)
router.register(r'manteniento', MantenimientoViewSet)
router.register(r'historial_ambiente', HistorialAmbienteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]