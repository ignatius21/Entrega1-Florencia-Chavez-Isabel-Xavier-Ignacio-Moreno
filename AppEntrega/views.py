

import email
from django.shortcuts import redirect, render
from django.http import HttpResponse

from AppEntrega.forms import libroForm, usuarioForm

from .models import *
# Create your views here.

def inicio(request):
    return render(request,'AppEntrega/inicio.html')



def biblioteca(request):
    return render(request,'AppEntrega/biblioteca.html',
    {'biblioteca': Libros.objects.all()})




def usuarios(request):
    return render(request,'AppEntrega/usuarios.html',
    {'usuarios': Usuarios.objects.all()})



def contacto(request):
    return render(request,'AppEntrega/contacto.html')







def formularioLibro(request):
    if request.method == 'POST':
        formularioLibro = libroForm(request.POST)
        if formularioLibro.is_valid():
            data = formularioLibro.cleaned_data
            Libros.objects.create(nombre=data['Nombre'],autor=data['Autor'],genero=data['Genero'])
            return redirect('inicio')
    else:    
        formularioLibro = libroForm()    
    return render(request,'AppEntrega/formularioLibro.html',{'formularioLibro': formularioLibro})





def buscarLibro(request):
    return render(request,'AppEntrega/buscarLibro.html') 


   
    

def RespuestaLibro(request):
    if request.GET['libro']:
        nombre = request.GET["libro"]
        libro= Libros.objects.filter(nombre__icontains=nombre)
        return render(request,'AppEntrega/respuestaLibro.html',{'nombres':nombre,'libros':libro})
    else:
        respuesta = 'Ingrese los datos nuevamente'
    return render(request,'AppEntrega/RespuestaLibro.html',{"respuesta": respuesta})       





def formularioUsuarios(request):
    if request.method == 'POST':
        formulario = usuarioForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            Usuarios.objects.create(nombre=data['Nombre'],apellido=data['Apellido'],email=data['Email'])
            return redirect('usuarios')
    else:    
        formularioUsuario = usuarioForm()    
    return render(request,'AppEntrega/formularioUsuarios.html',{'formularioUsuarios': formularioUsuario})

        
    





   


