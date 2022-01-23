from django.db import models

# Create your models here.

class Libros(models.Model):
    nombre = models.CharField(max_length=15)
    autor = models.CharField(max_length=20)
    genero = models.CharField(max_length=20)
    def __str__(self):
        return f' {self.nombre} / Autor: ({self.autor}) / Genero: ({self.genero})'


class Nosotros(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    email = models.EmailField()
    def __str__(self):
        return f'Hola yo soy {self.nombre} {self.apellido} y mi correo es {self.email}'



class Contacto(models.Model):
    telefono = models.IntegerField()
    email = models.EmailField()



