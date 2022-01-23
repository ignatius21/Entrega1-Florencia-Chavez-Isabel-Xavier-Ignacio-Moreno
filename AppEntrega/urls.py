from django.urls import path

from AppEntrega.views import Respuesta, biblioteca, buscarLibro, inicio,nosotros,contacto,formulario


urlpatterns = [
    path('inicio',inicio,name='inicio'),
    path('biblioteca',biblioteca,name='biblioteca'),
    path('nosotros',nosotros,name='nosotros'),
    path('contacto',contacto,name='contacto'),
    path('formulario',formulario,name='formulario'),
    path('buscarLibro',buscarLibro,name='buscarLibro'),
    path('respuesta',Respuesta,name='respuesta'),

    
    
]