from django.db import models
from django.contrib.auth.models import User

class Reservacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    tipo_habitacion = models.CharField(max_length=50)
    numero_huespedes = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.usuario.username}: {self.fecha_entrada} to {self.fecha_salida}"
