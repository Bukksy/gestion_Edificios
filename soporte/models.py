from django.db import models
from usuarios.models import Usuario

class Tickets(models.Model):
    nombre_residente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=[('pendiente', 'Pendiente'), ('resuelto', 'Resuelto')], default='pendiente')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ticket de {self.nombre_residente.username}: {self.estado}"
