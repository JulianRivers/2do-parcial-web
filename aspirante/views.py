from django.shortcuts import render, redirect
from .models import *
from .forms import*

# Create your views here.
def  index(request):
    return render(request, 'index.html')

def registrar_aspirante(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        tipo_documento = request.POST['tipo_documento']
        numero_documento = request.POST['numero_documento']
        profesion = request.POST['profesion']
        ciudad = request.POST['ciudad']
        edad = request.POST['edad']
        form = registrarAspirante(request.POST)
        if form.is_valid():
            Aspirante.objects.create(nombre=nombre, apellido=apellido, tipo_documento=tipo_documento, 
                                    numero_documento=numero_documento, profesion=profesion, ciudad=ciudad, edad=edad)
            return redirect('aspirante:index')
    else:
        form = registrarAspirante()
    context = {'form': form}
    return render(request, 'registrar.html', context)

def listar(request):
    aspirantes = Aspirante.objects.all()
    context = {'aspirantes': aspirantes}
    return render(request, 'listado.html', context)
