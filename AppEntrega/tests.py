from django.test import TestCase

from AppEntrega.models import Usuarios

# Create your tests here.


class UsuarioTestCase(TestCase):
    def test_crear_usuario(self):
        usuarios = Usuarios(nombre='nombre',apellido='apellido',email='email')
        usuarios.save()

        usuarios_en_base = Usuarios.objects.get(id=usuarios.id)

        self.assertEquals(usuarios_en_base.nombre,'nombre')
        self.assertEquals(usuarios_en_base.apellido,'apellido')
        self.assertEquals(usuarios_en_base.email,'email')

