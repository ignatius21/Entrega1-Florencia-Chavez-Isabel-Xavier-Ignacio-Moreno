from django.urls import path


from AppEntrega.views import Respuesta, biblioteca, buscarLibro, formularioUsuarios, inicio,contacto,formulario,usuarios


urlpatterns = [
    path('inicio',inicio,name='inicio'),
    path('biblioteca',biblioteca,name='biblioteca'),
    path('usuarios',usuarios,name='usuarios'),
    path('contacto',contacto,name='contacto'),
    path('formulario',formulario,name='formulario'),
    path('buscarLibro',buscarLibro,name='buscarLibro'),
    path('respuesta',Respuesta,name='respuesta'),
    path('formularioUsuarios',formularioUsuarios,name='formularioUsuarios'),

    
    
]