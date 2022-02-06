from django.db import models
# Create your models here.

class Libros(models.Model): 
    nombre = models.CharField(max_length=15)
    autor = models.CharField(max_length=15)
    genero = models.CharField(max_length=15)
    def __str__(self):
        return f' Nombre del libro: "{self.nombre}" / Autor: ({self.autor}) / Genero: ({self.genero})'


class Usuarios(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    email = models.EmailField()
    def __str__(self):
        return f'Usuario:  {self.nombre} '



class Donativo(models.Model):
    nombre = models.CharField(max_length=15)
    donativo = models.PositiveIntegerField()
    def __str__(self):
        return f'{self.nombre} ha donado ${self.donativo}...muchas gracias!!!'
    



