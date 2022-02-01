from django.forms import EmailField, Form,CharField, IntegerField

class libroForm(Form):
    Nombre = CharField()
    Autor = CharField()
    Genero = CharField()

class usuarioForm(Form):
    nombre = CharField()
    apellido = CharField()
    email = EmailField()



class donativoForm(Form):
    Nombre = CharField()
    Monto = IntegerField()
    
