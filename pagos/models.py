from django.db import models
from usuarios.models import Usuario

class Pago(models.Model):
    nombre_residente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pago de {self.monto} por {self.nombre_residente.username}"