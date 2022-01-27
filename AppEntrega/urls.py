from django.urls import path


from AppEntrega.views import RespuestaLibro, biblioteca, borrarUsuario, buscarDonativo, buscarLibro, buscarUsuario, formularioDonativo, formularioLibro, formularioUsuarios, inicio,donativo, respuestaDonativo, respuestaUsuario,usuarios


urlpatterns = [
    path('inicio',inicio,name='inicio'),
    path('biblioteca',biblioteca,name='biblioteca'),
    path('usuarios',usuarios,name='usuarios'),
    path('donativo',donativo,name='donativo'),
    path('formularioLibro',formularioLibro,name='formularioLibro'),
    path('buscarLibro',buscarLibro,name='buscarLibro'),
    path('respuestaLibro',RespuestaLibro,name='respuestaLibro'),
    path('formularioUsuarios',formularioUsuarios,name='formularioUsuarios'),
    path('buscarUsuario',buscarUsuario,name='buscarUsuario'),
    path('respestaUsuario',respuestaUsuario,name='respuestaUsuario'),
    path('buscarDonativo',buscarDonativo,name='buscarDonativo'),
    path('formularioDonativo',formularioDonativo,name='formularioDonativo'),
    path('respuestaDonativo',respuestaDonativo,name='respuestaDonativo'),
    path('borrarUsuario/delete/<id_usuario>',borrarUsuario,name='borrarUsuario'),
    

    
    
]