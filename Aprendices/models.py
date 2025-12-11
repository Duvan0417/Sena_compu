from django.db import models
from Computadores.models import Computador
from django.contrib.auth.models import User

class Aprendiz(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    tipo_documento = models.CharField(max_length=50)
    documento = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    num_ficha = models.CharField(max_length=20)
    programa_formacion = models.CharField(max_length=150)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Uso_computador(models.Model):

    ID_aprendiz = models.ForeignKey(Aprendiz, on_delete=models.CASCADE)
    ID_computador = models.ForeignKey(Computador, on_delete=models.CASCADE)
    ID_User = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_final = models.DateField(null=True, blank=True)
    hora_inicio = models.TimeField(null=True, blank=True)    
    hora_final = models.TimeField(null=True, blank=True)
