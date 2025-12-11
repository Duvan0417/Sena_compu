"""
URL configuration for Sena_compu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rutas de la app Usuarios
    path('', include('Usuarios.urls')),  
    
    # Rutas de la app Ambientes (aquí agregamos tu nueva ruta)
    path('api/', include('ambientes.urls')),

    path('api/', include('Computadores.urls')),

    path('api/', include('Aprendices.urls')),  

    # JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
