from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return render(request,'AppEntrega/inicio.html')
def productos(request):
    return render(request,'AppEntrega/productos.html')
def nosotros(request):
    return render(request,'AppEntrega/nosotros.html')
def contacto(request):
    return render(request,'AppEntrega/contacto.html')
def servicios(request):
    return render(request,'AppEntrega/servicios.html')