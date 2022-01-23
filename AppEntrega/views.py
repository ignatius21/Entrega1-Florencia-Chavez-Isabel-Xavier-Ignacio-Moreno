

from django.shortcuts import redirect, render
from django.http import HttpResponse

from AppEntrega.forms import Productoform

from .models import *
# Create your views here.

def inicio(request):
    return render(request,'AppEntrega/inicio.html')



def libros(request):
    return render(request,'AppEntrega/libros.html',
    {'libros': Libros.objects.all()})




def nosotros(request):
    return render(request,'AppEntrega/nosotros.html',
    {'nosotros': Nosotros.objects.all()})



def contacto(request):
    return render(request,'AppEntrega/contacto.html')







def formulario(request):
    if request.method == 'POST':
        formulario = Productoform(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            Libros.objects.create(nombre=data['nombre'],numeroSerie=data['numeroSerie'],numeroLote=data['numeroLote'])
            return redirect('inicio')
    else:    
        formulario = Productoform()    
    return render(request,'AppEntrega/formulario.html',{'formulario': formulario})

def buscarLibro(request):
    return render(request,'AppEntrega/buscarLibro.html') 

def Respuesta(request):
        nombre = request.GET["libro"]
        libro= Libros.objects.filter(nombre=nombre)
        return render(request,'AppEntrega/respuesta.html',{'nombres':nombre,'libros':libro})
        
    





   


