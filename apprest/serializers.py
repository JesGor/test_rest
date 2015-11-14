from rest_framework import serializers
from .models import Empresa, Calificacion

class EmpresaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Empresa
		fields = ("nombre", "ciudad", "sector",)
		
class CalificacionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Calificacion
		fields = ("alumno", "calificacion", "empresa",)

