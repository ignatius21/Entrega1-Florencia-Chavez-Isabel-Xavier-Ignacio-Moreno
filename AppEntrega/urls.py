from django.urls import path


from AppEntrega.views import BibliotecaCreateView,inicio_login, BibliotecaListView, DonativoCreateView, DonativoListView, RespuestaLibro, UsuarioCreateView, UsuarioDeleteView,UsuarioDetailView, UsuarioListView, UsuarioUpdateView,buscarDonativo, buscarLibro, buscarUsuario,inicio, respuestaDonativo, respuestaUsuario


urlpatterns = [
    path('inicio',inicio,name='inicio'),
    path('',inicio_login,name='login'),
    


    path('donativo',DonativoListView.as_view(),name='donativo'),
    path('formularioDonativo',DonativoCreateView.as_view(),name='formularioDonativo'),
    path('buscarDonativo',buscarDonativo,name='buscarDonativo'),
    path('respuestaDonativo',respuestaDonativo,name='respuestaDonativo'),



    path('usuarios',UsuarioListView.as_view(),name='usuarios'),
    path('ingresarUsuarios',UsuarioCreateView.as_view(),name='ingresarUsuarios'),
    path('actualizarUsuario/<pk>',UsuarioUpdateView.as_view(),name='actualizarUsuario'),
    path('borrarUsuario/<pk>',UsuarioDeleteView.as_view(),name='borrarUsuario'),
    path('verUsuario/<pk>',UsuarioDetailView.as_view(),name='verUsuario'),
    path('buscarUsuario',buscarUsuario,name='buscarUsuario'),
    path('respestaUsuario',respuestaUsuario,name='respuestaUsuario'),




    path('ingresarLibros',BibliotecaCreateView.as_view(),name='ingresarLibros'),
    path('biblioteca',BibliotecaListView.as_view(),name='biblioteca'),
    path('respuestaLibro',RespuestaLibro,name='respuestaLibro'),
    path('buscarLibro',buscarLibro,name='buscarLibro'),

    
    
]