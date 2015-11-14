from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Empresa, Calificacion
from .serializers import EmpresaSerializer, CalificacionSerializer

class JSONResponse(HttpResponse):
	"""
	An HttpResponse that renders its content into JSON.
	"""
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)
        
@csrf_exempt
def lista_empresas(request):
	"""
	List las empresas, o crea una
	"""
	if request.method == 'GET':
		empresas = Empresa.objects.all()
		serializer = EmpresaSerializer(empresas, many=True)
		return JSONResponse(serializer.data)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = EmpresaSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data, status=201)
		return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def empresa(request, pk):
	try:
		empresa = Empresa.objects.get(pk=pk)
	except Empresa.DoesNotExist:
		return JSONResponse(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		calificaciones = empresa.calificacion_set.all()
		serializer = CalificacionSerializer(calificaciones, many=True)
		return JSONResponse(serializer.data)

	elif request.method == 'DELETE':
		empresa.delete()
		return JSONResponse(status=status.HTTP_204_NO_CONTENT)
		

