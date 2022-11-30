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
            return redirect('aspirante:index')
    else:
        form = registrarAspirante()
    context = {'form': form}
    return render(request, 'registrar.html', context)

#no sirve
def listar(request):
    aspirantes = EvaluacionAdmision.objects.order_by(Lower('puntaje_total_puntos').desc())
    context = {'aspirantes': aspirantes}
    return render(request, 'listado.html', context)

def listar_cargo(request, cargo=2):
    evaluaciones = EvaluacionAdmision.objects.all()
    listado_aspirantes = []
    aspirante = None
    for evaluacion in evaluaciones:
        if evaluacion.cargo_id==cargo and evaluacion.estado_admision_id==1:
            aspirante = f"{evaluacion.aspirante}" + "{nombre :"+ f"{evaluacion.aspirante.nombre}" 
            + ",apellido :"+ f"{evaluacion.aspirante.apellido}" + ",tipo_documento :"+ f"{evaluacion.aspirante.tipo_documento}" 
            + ",numero_documento :"+ f"{evaluacion.aspirante.numero_documento}" + ",profesion :"+ f"{evaluacion.aspirante.profesion}" 
            + ",ciudad :"+ f"{evaluacion.aspirante.ciudad}" + ",edad :"+ f"{evaluacion.aspirante.edad}" + ",cargo :"+ f"{evaluacion.cargo.nombre}"
        listado_aspirantes.append(aspirante)
        print(evaluacion.estado_admision)
    return JsonResponse(json.dumps(listado_aspirantes), safe=False)
