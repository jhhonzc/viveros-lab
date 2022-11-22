from django.test import TestCase
from .models import Usuario, UsuarioManager

# Create your tests here.
class UsuarioModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Usuario.objects.create_user(email='algo@gmail.com',username='rambo', nombres='Julian', apellidos='Alvarez')

    def test_nombre_usuario(self):
        usuario = Usuario.objects.get(id=1)
        nombre_u = usuario.nombres
        self.assertEquals(nombre_u, 'Julian')
    
    def test_username_usuario(self):
        usuario = Usuario.objects.get(id=1)
        username_u = usuario.username
        self.assertEquals(username_u, 'rambo')
    
    def test_apellidos_usuario(self):
        usuario = Usuario.objects.get(id=1)
        apellidos_u = usuario.apellidos
        self.assertEquals(apellidos_u, 'Alvarez')
    
    def test_email_usuario(self):
        usuario = Usuario.objects.get(id=1)
        email_u = usuario.email
        self.assertEquals(email_u,'algo@gmail.com')