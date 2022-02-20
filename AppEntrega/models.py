from django.db.models import Model,CASCADE,ImageField,ForeignKey
from django.contrib.auth.models import User
from django.db.models.fields import CharField,EmailField,PositiveIntegerField



# Create your models here.

class Libros(Model): 
    nombre = CharField(max_length=15)
    autor = CharField(max_length=15)
    genero = CharField(max_length=15)
    def __str__(self):
        return f' Nombre del libro: "{self.nombre}" / Autor: ({self.autor}) / Genero: ({self.genero})'


class Usuarios(Model):
    nombre = CharField(max_length=15)
    apellido = CharField(max_length=15)
    email = EmailField()
    def __str__(self):
        return f'Usuario:  {self.nombre} '



class Donativo(Model):
    nombre = CharField(max_length=15)
    donativo = PositiveIntegerField()
    def __str__(self):
        return f'{self.nombre} ha donado ${self.donativo}...muchas gracias!!!'
    

class Avatar(Model):
    user = ForeignKey(User,on_delete=CASCADE)
    imagen = ImageField(upload_to='avatares',null=True,blank=True)

