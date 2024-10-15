from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    ROL_CHOICES = [
        ('administrador', 'Administrador'),
        ('portero', 'Portero'),
        ('residente', 'Residente'),
        ('arrendatario', 'Arrendatario'),
        ('administrativo', 'Administrativo'),
    ]
    rol = models.CharField(max_length=20, choices=ROL_CHOICES)
    direccion = models.CharField(max_length=255, blank=True, null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='grupos_usuarios', 
        blank=True
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuarios_permitidos',
        blank=True
    )

    def __str__(self):
        return f"{self.username} - {self.rol}"
