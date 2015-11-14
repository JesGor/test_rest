from rest_framework import status
from rest_framework.test import APITestCase
from .models import Empresa, Calificacion
from .views import *

class EmpresaRESTTests(APITestCase):
	def test_crear_empresa(self):
		data = { "nombre" : "test", "ciudad" : "ciudadtest", "sector" : "sectortest" }
		response = self.client.post("/empresas/", data, format="json")
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Empresa.objects.get().nombre, "test")
		print("Creada empresa correctamente con interfaz REST")
		
	def test_mostrar_empresas(self):
		emp1 = Empresa(nombre="test", ciudad="ciudadtest", sector="sectortest")
		emp1.save()
		emp2 = Empresa(nombre="test2", ciudad="ciudadtest2", sector="sectortest2")
		emp2.save()
		response = self.client.get("/empresas/")
		self.assertEqual(response.content, b'[{"nombre":"test","ciudad":"ciudadtest","sector":"sectortest"},{"nombre":"test2","ciudad":"ciudadtest2","sector":"sectortest2"}]')
		print("Listado de empresas realizado con éxito mediante interfaz REST")
		
class CalificacionRESTTest(APITestCase):
	def test_mostrar_calificaciones(self):
		e = Empresa(nombre="test", ciudad="ciudadtest", sector="sectortest")
		e.save()
		cal1 = Calificacion(alumno="alumtest", calificacion=10, empresa=e)
		cal1.save()
		cal2 = Calificacion(alumno="alum2test", calificacion=0, empresa=e)
		cal2.save()
		response = self.client.get("/empresas/1/")
		self.assertEqual(response.content, b'[{"alumno":"alumtest","calificacion":10,"empresa":1},{"alumno":"alum2test","calificacion":0,"empresa":1}]')
		print("Listado de calificacion de una empresa exitoso con interfaz REST")

# Create your tests here.
