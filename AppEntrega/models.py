from django.db import models

# Create your models here.

class Productos(models.Model):
    nombre = models.CharField(max_length=15)
    numeroSerie = models.IntegerField()
    numeroLote = models.IntegerField()
    def __str__(self):
        return f' {self.nombre} / Numero de serie: ({self.numeroSerie}) / Numero de lote: ({self.numeroLote})'
class Nosotros(models.Model):
    cargo = models.CharField(max_length=15)
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    email = models.EmailField()
class Contacto(models.Model):
    oficina = models.CharField(max_length=15)
    telefono = models.IntegerField()
    email = models.EmailField()
class Servicios(models.Model):
    nombre = models.CharField(max_length=15)