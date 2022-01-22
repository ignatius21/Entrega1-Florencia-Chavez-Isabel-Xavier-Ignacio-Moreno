
from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import *
# Create your views here.

def inicio(request):
    return render(request,'AppEntrega/inicio.html')



def productos(request):
    return render(request,'AppEntrega/productos.html',
    {'productos': Productos.objects.all()})




def nosotros(request):
    return render(request,'AppEntrega/nosotros.html')



def contacto(request):
    return render(request,'AppEntrega/contacto.html')



def servicios(request):
    return render(request,'AppEntrega/servicios.html')



def formulario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        numeroSerie = request.POST['numeroSerie']
        numeroLote = request.POST['numeroLote']
        print(request.POST)
        Productos.objects.create(nombre=nombre,numeroSerie=numeroSerie,numeroLote=numeroLote)
        return redirect('productos')
        
    return render(request,'AppEntrega/formulario.html')



