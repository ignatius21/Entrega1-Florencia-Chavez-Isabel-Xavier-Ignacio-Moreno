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
    nombre = request.GET["libro"]
    libro= Libros.objects.filter(nombre__icontains=nombre)
    return render(request,'AppEntrega/respuestaLibro.html',{'nombres':nombre,'libros':libro})









def buscarUsuario(request):
    return render(request,'AppEntrega/buscarUsuario.html')    


def respuestaUsuario(request):
    nombre = request.GET["usuario"]
    usuario= Usuarios.objects.filter(nombre__icontains=nombre)
    return render(request,'AppEntrega/respuestaUsuario.html',{'nombres':nombre,'usuarios':usuario})
      






def formularioDonativo(request):
    if request.method == 'POST':
        formularioDonativo = donativoForm(request.POST)
        if formularioDonativo.is_valid():
            data = formularioDonativo.cleaned_data
            Donativo.objects.create(nombre=data['Nombre'], donativo=data['Monto'])
            return redirect('donativo')
    else:    
        formularioDonativo = donativoForm()    
    return render(request,'AppEntrega/formularioDonativo.html',{'formularioDonativo': formularioDonativo})


def buscarDonativo(request):
    return render(request,'AppEntrega/buscarDonativo.html')    


def respuestaDonativo(request):
    donativo = request.GET["donativo"]
    monto = Donativo.objects.filter(nombre=donativo)
    return render(request,'AppEntrega/respuestaDonativo.html',{'nombres':donativo,'montos':monto})
        



        
def borrarUsuario(request,id_usuario):
    usuario = Usuarios.objects.get(id=id_usuario)
    usuario.delete()

    return redirect('usuarios') 


# def actualizarUsuario(request,id_usuario):
#     usuario = Usuarios.objects.get(id=id_usuario)
#     if request.method == 'POST':
#         formulario = usuarioForm(request.POST)
        

#         if formulario.is_valid():
#             data = formulario.cleaned_data

#             usuario.nombre = data['nombre'],
#             usuario.apellido = data['apellido'],
#             usuario.email = data['email']
#             usuario.save()
#             return redirect('usuarios')
#     else:    
#         formulario = usuarioForm(model_to_dict(usuario))    
#     return render(request,'AppEntrega/formularioActualizar.html',{'formularioActualizar': formulario})








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




   


