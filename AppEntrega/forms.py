from django.forms import Form,CharField,IntegerField

class Productoform(Form):
    Nombre = CharField()
    Autor = IntegerField()
    Genero = IntegerField()