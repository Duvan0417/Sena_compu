from django.db import models
from ambientes.models import Ambiente
from django.contrib.auth.models import User


class Computador(models.Model):
    Estados = [
        ('Disponible', 'Disponible'),
        ('En uso', 'En uso'),
        ('Mantenimiento', 'Mantenimiento'),
        ('Fuera de servicio', 'Fuera de servicio'),
    ]
    serial_number = models.CharField(max_length=50, unique=True)
    marca = models.CharField(max_length=100)
    estado = models.CharField(max_length=100, choices=Estados, default='Disponible')
    modelo = models.CharField(max_length=100)
    procesador = models.CharField(max_length=100)
    ram = models.CharField(max_length=70)
    almacenamiento = models.CharField(max_length=70)
    observaciones = models.TextField(blank=True, null=True)
    fecha_adquisicion = models.DateField()

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.serial_number}"
    
class Compu_dañados(models.Model):
    gravedad_estado = [
        ('Baja','Baja'),
        ('Media','Media'),
        ('Alta','Alta')
    ]
    estado_inicial = [
        ('Pendiente', 'Pendiente'),
        ('En proceso', 'En proceso'),
        ('Reparado', 'Reparado')
    ]
    descripcion_daño = models.TextField(max_length=500)
    fecha_reporte = models.DateField(auto_now_add=True)
    gravedad_daño = models.CharField(max_length=50, choices=gravedad_estado, default='Media')
    estado_inicial = models.CharField(max_length=100, choices=estado_inicial, default='Pendiente')
    ID_computador = models.OneToOneField(Computador, on_delete=models.CASCADE)

class Mantenimiento(models.Model):
    descripcion =  models.TextField(max_length=500)
    fecha_ingreso = models.DateField(auto_now_add=True)
    fecha_salida = models.DateField(null=True, blank=True)
    ID_computador = models.ForeignKey(Computador, on_delete=models.CASCADE)

class Historial_Ambiente(models.Model):
    ID_computador = models.ForeignKey(Computador, on_delete=models.CASCADE)
    ID_ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    ID_user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_asignacion = models.DateField(auto_now_add=True)
    fecha_remocion = models.DateField(null=True, blank=True)