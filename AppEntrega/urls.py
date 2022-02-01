from django.urls import path


from AppEntrega.views import RespuestaLibro, UsuarioCreateView, UsuarioListView, UsuarioUpdateView,biblioteca, borrarUsuario, buscarDonativo, buscarLibro, buscarUsuario, formularioDonativo, formularioLibro, inicio,donativo, respuestaDonativo, respuestaUsuario


urlpatterns = [
    #path('actualizarUsuario/<id_usuario>',actualizarUsuario,name='actualizarUsuario'),
    # path('usuarios',usuarios,name='usuarios'),
    # path('formularioUsuarios',formularioUsuarios,name='formularioUsuarios'),
    path('inicio',inicio,name='inicio'),
    path('biblioteca',biblioteca,name='biblioteca'),
    path('donativo',donativo,name='donativo'),
    path('formularioLibro',formularioLibro,name='formularioLibro'),
    path('buscarLibro',buscarLibro,name='buscarLibro'),
    path('respuestaLibro',RespuestaLibro,name='respuestaLibro'),
    path('buscarUsuario',buscarUsuario,name='buscarUsuario'),
    path('respestaUsuario',respuestaUsuario,name='respuestaUsuario'),
    path('buscarDonativo',buscarDonativo,name='buscarDonativo'),
    path('formularioDonativo',formularioDonativo,name='formularioDonativo'),
    path('respuestaDonativo',respuestaDonativo,name='respuestaDonativo'),
    path('borrarUsuario/<id_usuario>',borrarUsuario,name='borrarUsuario'),
    path('usuarios',UsuarioListView.as_view(),name='usuarios'),
    path('ingresarUsuarios',UsuarioCreateView.as_view(),name='ingresarUsuarios'),
    path('actualizarUsuario/<pk>',UsuarioUpdateView.as_view(),name='actualizarUsuario'),

    
    
]