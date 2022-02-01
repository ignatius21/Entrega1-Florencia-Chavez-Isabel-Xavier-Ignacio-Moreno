from django.urls import path


from AppEntrega.views import RespuestaLibro, UsuarioCreateView, UsuarioDeleteView,UsuarioDetailView, UsuarioListView, UsuarioUpdateView,biblioteca,buscarDonativo, buscarLibro, buscarUsuario, formularioDonativo, formularioLibro, inicio,donativo, respuestaDonativo, respuestaUsuario


urlpatterns = [
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
    path('usuarios',UsuarioListView.as_view(),name='usuarios'),
    path('ingresarUsuarios',UsuarioCreateView.as_view(),name='ingresarUsuarios'),
    path('actualizarUsuario/<pk>',UsuarioUpdateView.as_view(),name='actualizarUsuario'),
    path('borrarUsuario/<pk>',UsuarioDeleteView.as_view(),name='borrarUsuario'),
    path('verUsuario/<pk>',UsuarioDetailView.as_view(),name='verUsuario'),

    
    
]