from django.forms import Form,CharField

class libroForm(Form):
    Nombre = CharField()
    Autor = CharField()
    Genero = CharField()