from django.db import models


# Create your models here.

class Servicio(models.Model):
    ESTADOS = (
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
        ('pendiente', 'Pendiente'),
    )

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='activo')
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
