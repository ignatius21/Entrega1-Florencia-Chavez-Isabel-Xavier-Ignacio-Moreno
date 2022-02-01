from django.forms import model_to_dict
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from AppEntrega.forms import donativoForm, libroForm, usuarioForm
from .models import *
from django.views.generic import ListView,DetailView,DeleteView,CreateView,UpdateView


# Create your views here.

def inicio(request):
    return render(request,'AppEntrega/inicio.html')

def biblioteca(request):
    return render(request,'AppEntrega/biblioteca.html',
    {'biblioteca': Libros.objects.all()})

def usuarios(request):
    return render(request,'AppEntrega/usuarios.html',
    {'usuarios': Usuarios.objects.all()})

def donativo(request):
    return render(request,'AppEntrega/donativo.html',
    {'donativos':Donativo.objects.all()})








class BibliotecaCreateView(CreateView):
    model = Libros
    success_url = reverse_lazy('biblioteca')
    fields = ['nombre','autor','genero']
    template_name = 'AppEntrega/libro_form.html'

class BibliotecaListView(ListView):
    model = Libros
    template_name = 'AppEntrega/biblioteca.html'
    context_object_name = 'biblioteca'    


def buscarLibro(request):
    return render(request,'AppEntrega/buscarLibro.html') 

   
def RespuestaLibro(request):
    nombre = request.GET["libro"]
    libro= Libros.objects.filter(nombre__icontains=nombre)
    return render(request,'AppEntrega/respuestaLibro.html',{'nombres':nombre,'libros':libro})









class DonativoCreateView(CreateView):
    model = Donativo
    success_url = reverse_lazy('donativo')
    fields = ['nombre','donativo']
    template_name = 'AppEntrega/donativo_form.html'  

class DonativoListView(ListView):
    model = Donativo
    template_name = 'AppEntrega/donativo.html'
    context_object_name = 'donativos'

def buscarDonativo(request):
    return render(request,'AppEntrega/buscarDonativo.html')    

def respuestaDonativo(request):
    donativo = request.GET["donativo"]
    monto = Donativo.objects.filter(nombre=donativo)
    return render(request,'AppEntrega/respuestaDonativo.html',{'nombres':donativo,'montos':monto})
        







class UsuarioListView(ListView):
    model = Usuarios
    template_name = 'AppEntrega/usuarios.html'
    context_object_name = 'usuarios'

class UsuarioDetailView(DetailView):
    model = Usuarios
    template_name = 'AppEntrega/ver_usuario.html'


class UsuarioCreateView(CreateView):
    model = Usuarios
    success_url = reverse_lazy('usuarios')
    fields = ['nombre','apellido','email']
    template_name = 'AppEntrega/usuario_form.html'


class UsuarioUpdateView(UpdateView):
    model = Usuarios
    success_url = reverse_lazy('usuarios')
    fields = ['nombre','apellido','email']
    template_name = 'AppEntrega/formActualizar.html'  

class UsuarioDeleteView(DeleteView):
    model = Usuarios
    success_url = reverse_lazy('usuarios')
    template_name = 'AppEntrega/usuario_confirm_delete.html'


def buscarUsuario(request):
    return render(request,'AppEntrega/buscarUsuario.html')    


def respuestaUsuario(request):
    nombre = request.GET["usuario"]
    usuario= Usuarios.objects.filter(nombre__icontains=nombre)
    return render(request,'AppEntrega/respuestaUsuario.html',{'nombres':nombre,'usuarios':usuario})


   


