from django.forms import EmailField, Form,CharField

class libroForm(Form):
    Nombre = CharField()
    Autor = CharField()
    Genero = CharField()

class usuarioForm(Form):
    Nombre = CharField()
    Apellido = CharField()
    Email = EmailField()
