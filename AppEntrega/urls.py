from django.urls import path


from AppEntrega.views import RespuestaLibro, biblioteca, buscarLibro, formularioLibro, formularioUsuarios, inicio,contacto,usuarios


urlpatterns = [
    path('inicio',inicio,name='inicio'),
    path('biblioteca',biblioteca,name='biblioteca'),
    path('usuarios',usuarios,name='usuarios'),
    path('contacto',contacto,name='contacto'),
    path('formularioLibro',formularioLibro,name='formularioLibro'),
    path('buscarLibro',buscarLibro,name='buscarLibro'),
    path('respuestaLibro',RespuestaLibro,name='respuestaLibro'),
    path('formularioUsuarios',formularioUsuarios,name='formularioUsuarios'),

    
    
]