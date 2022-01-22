from django.urls import path
from AppEntrega.views import inicio,productos,nosotros,contacto,servicios,formulario

urlpatterns = [
    path('inicio',inicio,name='inicio'),
    path('productos',productos,name='productos'),
    path('nosotros',nosotros,name='nosotros'),
    path('contacto',contacto,name='contacto'),
    path('servicios',servicios,name='servicios'),
    path('formulario',formulario,name='formulario'),
    
]