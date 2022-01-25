from django.urls import path


from AppEntrega.views import RespuestaLibro, biblioteca, buscarLibro, buscarUsuario, formularioLibro, formularioUsuarios, inicio,contacto, respuestaUsuario,usuarios


urlpatterns = [
    path('inicio',inicio,name='inicio'),
    path('biblioteca',biblioteca,name='biblioteca'),
    path('usuarios',usuarios,name='usuarios'),
    path('contacto',contacto,name='contacto'),
    path('formularioLibro',formularioLibro,name='formularioLibro'),
    path('buscarLibro',buscarLibro,name='buscarLibro'),
    path('respuestaLibro',RespuestaLibro,name='respuestaLibro'),
    path('formularioUsuarios',formularioUsuarios,name='formularioUsuarios'),
    path('buscarUsuario',buscarUsuario,name='buscarUsuario'),
    path('respestaUsuario',respuestaUsuario,name='respuestaUsuario'),

    
    
]