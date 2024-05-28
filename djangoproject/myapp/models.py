from django.db import models
from django.contrib.auth.models import User

class Reservacion(models.Model):
    HABITACION_CHOICES = [
        ('individual', 'Individual'),
        ('doble', 'Doble'),
        ('suite', 'Suite'),
        ('penhouse','Penhouse')
    ]
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    #nombre_completo = models.CharField(max_length=50)
    #direccion = models.CharField(max_length=50)
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    tipo_habitacion = models.CharField(max_length=50, choices=HABITACION_CHOICES)
    numero_huespedes = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.usuario.username}: {self.fecha_entrada} to {self.fecha_salida}"