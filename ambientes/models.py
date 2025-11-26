from django.db import models
from django.contrib.auth.models import User


class Ambiente(models.Model):
    nombre_ambiente = models.CharField(max_length=100, unique=True)
    ubicacion = models.CharField(max_length=200)
    capacidad = models.IntegerField()
    ID_user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    