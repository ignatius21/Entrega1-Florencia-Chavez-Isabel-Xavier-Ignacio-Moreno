from django.forms import EmailField, Form,CharField, IntegerField,ImageField

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

class AvatarForm(Form):
    imagen = ImageField(required=True)
    
