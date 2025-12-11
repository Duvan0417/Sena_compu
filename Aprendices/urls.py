from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import (
    UsoComputadorViewSet,
    AprendizViewSet
)

router = DefaultRouter()

router.register(r'aprendices', AprendizViewSet)
router.register(r'uso_computadores', UsoComputadorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]