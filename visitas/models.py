from django.db import models
from usuarios.models import Usuario

class Visita(models.Model):
    residente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='residente_visita')
    visitante_nombre = models.CharField(max_length=100)
    rut_visitante = models.CharField(max_length=9, default='12345678-9')
    fecha_entrada = models.DateTimeField(auto_now_add=True)
    fecha_salida = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Se registra la visita de: {self.visitante_nombre} a {self.residente.username}"

class Aviso(models.Model):
    residente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='residente_aviso')
    descripcion = models.TextField()
    fecha_recepcion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Aviso de ingreso para: {self.residente.username}"
 