
from django.shortcuts import redirect, render
from django.http import HttpResponse

from AppEntrega.forms import Productoform

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
        formulario = Productoform(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            Productos.objects.create(nombre=data['nombre'],numeroSerie=data['numeroSerie'],numeroLote=data['numeroLote'])
            return redirect('inicio')
    else:    
        formulario = Productoform()    
    return render(request,'AppEntrega/formulario.html',{'formulario': formulario})

def buscarProductos(request):
    return render(request,'AppEntrega/buscarproductos.html') 

def Respuesta(request):
    respuesta = f'Buscando producto:  {request.GET["producto"]}'
    return HttpResponse(respuesta)
    





   


