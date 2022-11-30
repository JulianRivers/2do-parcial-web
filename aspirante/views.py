from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.db.models.functions import Lower
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json
# Create your views here.

def index(request):
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
            aspirante = Aspirante.objects.create(nombre=nombre, apellido=apellido, tipo_documento=tipo_documento,
                                     numero_documento=numero_documento, profesion=profesion, ciudad=ciudad, edad=edad)
            admision = EstadoAdmision.objects.get(id=3)
            cargo = Cargo.objects.get(id=1)
            evaluacion = EvaluacionAdmision.objects.create(aspirante=aspirante, admision=admision,cargo=cargo)
            return redirect('aspirante:index')
    else:
        form = registrarAspirante()
    context = {'form': form}
    return render(request, 'registrar.html', context)

#no sirve
def listar(request):
    lista = []
    evaluaciones = EvaluacionAdmision.objects.order_by(Lower('total_puntos').desc())
    for evaluacion in evaluaciones:
        id_asp = evaluacion.aspirante_id
        aspirante = Aspirante.objects.get(id=id_asp)
        aspirante.puntaje = evaluacion.total_puntos
        lista.append(aspirante)
    context = {'aspirantes': lista}
    return render(request, 'listado.html', context)

def listar_cargo(request, cargo=2):
    evaluaciones = EvaluacionAdmision.objects.all()
    listado_aspirantes = []
    aspirante = None
    for evaluacion in evaluaciones:
        if evaluacion.cargo_id==cargo and evaluacion.admision_id==1:
            aspirante = Aspirante.objects.get(id=evaluacion.aspirante_id)
            listado_aspirantes.append(aspirante)
        print(aspirante)
    data = serializers.serialize('json', listado_aspirantes)
    return JsonResponse(data, safe=False)
