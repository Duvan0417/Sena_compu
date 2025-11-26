from django.db import models
from django.contrib.auth.models import User

class Consultas(models.Model):
    Estados = [
        ('Pendiente', 'Pendiente'),
        ('En proceso', 'En proceso'),
        ('Resuelta', 'Resuelta'),
    ]
    fecha_consulta = models.DateField(auto_now_add=True)
    descrip_Consulta = models.TextField(max_length=1200)
    respuesta_consulta = models.TextField(max_length=1200, null=True, blank=True)
    estado_consulta = models.CharField(max_length=100, default='Pendiente', choices=Estados)
    tiempo_respuesta = models.FloatField(null=True, blank=True)
    ID_usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Consulta {self.id} - Estado: {self.estado_consulta}"
    
    