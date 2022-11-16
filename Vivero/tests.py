from django.test import TestCase
from .models import Vivero, Municipio, Departamento, Productor

# Create your tests here.
class ViveroModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        productor = Productor.objects.create(
            numero_documento="12341234",
            nombre="John",
            apellido="Doe",
            direccion="Cra 1 # 234",
            email="johndoe@email.com",
            telefono="3211234567",
        )
        Departamento.objects.create(nombre_departamento="Risaralda")
        Municipio.objects.create(nombre_municipio="Dosquebradas", departamento_id="1")
        Vivero.objects.create(
            nombre_vivero="Yerba Mala",
            codigo="123",
            productor=productor,
            departamento=1,
            municipio=1,
        )

    def test_nombre_departamento(self):
        departamento = Departamento.objects.get(id=1)
        nombre_d = departamento.nombre_departamento
        self.assertEquals(nombre_d, "Risaralda")

    def test_nombre_municipio(self):
        municipio = Municipio.objects.get(id=1)
        nombre_m = municipio.nombre_municipio
        self.assertEquals(nombre_m, "Dosquebradas")

    def test_nombre_vivero(self):
        vivero = Vivero.objects.get(id=1)
        nombre_v = vivero.nombre_vivero
        self.assertEquals(nombre_v, "Yerba Mala")

    def test_codigo_vivero(self):
        vivero = Vivero.objects.get(id=1)
        codigo_v = vivero.codigo
        self.assertEquals(codigo_v, 123)