from django.shortcuts import render
from .models import *

# Create your views here.
def  index(request):
    return render(request, 'index.html')

def registrar_aspirante(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        tipo_documento = request.POST['tipo_documento']
        numero_documento = request.POST['numero_documento']
        profesion = request.FILES['profesion']
        ciudad = request.POST['ciudad']
        edad = request.POST['edad']

    return render(request, 'registrar.html')

def listar(request):
    aspirantes = Aspirante.objects.all()
    context = {'aspirantes': aspirantes}
    return render(request, 'listado.html', context)
