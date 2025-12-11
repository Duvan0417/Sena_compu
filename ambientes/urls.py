from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import AmbienteViewSet

router = DefaultRouter()
router.register(r'ambientes', AmbienteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
