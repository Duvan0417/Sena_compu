from rest_framework import routers
from django.urls import path
from .api import UserViewSet
from .views import register_user   # tu vista de registro

router = routers.DefaultRouter()
router.register(r'api/user', UserViewSet)

urlpatterns = [
    # rutas generadas automáticamente por el router
    *router.urls,

    # ruta personalizada para registrar usuarios
    path('api/register/', register_user, name='register'),
]