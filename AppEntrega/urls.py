from django.urls import path

from AppEntrega.views import Respuesta, buscarLibro, inicio,nosotros,contacto,formulario,libros


urlpatterns = [
    path('inicio',inicio,name='inicio'),
    path('libros',libros,name='libros'),
    path('nosotros',nosotros,name='nosotros'),
    path('contacto',contacto,name='contacto'),
    path('formulario',formulario,name='formulario'),
    path('buscarLibro',buscarLibro,name='buscarLibro'),
    path('respuesta',Respuesta,name='respuesta'),

    
    
]