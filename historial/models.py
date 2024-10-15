from django.db import models
from usuarios.models import Usuario

class Historial(models.Model):
    nombre_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    accion = models.CharField(max_length=255)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Acción de {self.nombre_usuario.username}: {self.accion}"