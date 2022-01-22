from django.forms import Form,CharField,IntegerField

class Productoform(Form):
    nombre = CharField()
    numeroSerie = IntegerField()
    numeroLote = IntegerField()