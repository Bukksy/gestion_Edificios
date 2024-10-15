from django.db import models
from usuarios.models import Usuario

class EspacioComun(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    espacio = models.ForeignKey(EspacioComun, on_delete=models.CASCADE)
    nombre_residente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_reserva = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"Reserva del espacio: {self.espacio.nombre} por {self.nombre_residente.username} el {self.fecha_reserva}"
