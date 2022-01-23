from django.forms import Form,CharField

class Productoform(Form):
    Nombre = CharField()
    Autor = CharField()
    Genero = CharField()