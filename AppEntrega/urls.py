from django.urls import path


from AppEntrega.views import BibliotecaCreateView,inicio_login, BibliotecaListView, DonativoCreateView, DonativoListView, RespuestaLibro, UsuarioCreateView, UsuarioDeleteView,UsuarioDetailView, UsuarioListView, UsuarioUpdateView,buscarDonativo, buscarLibro, buscarUsuario,inicio, respuestaDonativo, respuestaUsuario
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('inicio',login_required(inicio),name='inicio'),
    path('',inicio_login,name='login'),
    


    path('donativo',login_required(DonativoListView.as_view()),name='donativo'),
    path('formularioDonativo',login_required(DonativoCreateView.as_view()),name='formularioDonativo'),
    path('buscarDonativo',login_required(buscarDonativo),name='buscarDonativo'),
    path('respuestaDonativo',login_required(respuestaDonativo),name='respuestaDonativo'),



    path('usuarios',login_required(UsuarioListView.as_view()),name='usuarios'),
    path('ingresarUsuarios',login_required(UsuarioCreateView.as_view()),name='ingresarUsuarios'),
    path('actualizarUsuario/<pk>',login_required(UsuarioUpdateView.as_view()),name='actualizarUsuario'),
    path('borrarUsuario/<pk>',login_required(UsuarioDeleteView.as_view()),name='borrarUsuario'),
    path('verUsuario/<pk>',login_required(UsuarioDetailView.as_view()),name='verUsuario'),
    path('buscarUsuario',login_required(buscarUsuario),name='buscarUsuario'),
    path('respestaUsuario',login_required(respuestaUsuario),name='respuestaUsuario'),




    path('ingresarLibros',login_required(BibliotecaCreateView.as_view()),name='ingresarLibros'),
    path('biblioteca',login_required(BibliotecaListView.as_view()),name='biblioteca'),
    path('respuestaLibro',login_required(RespuestaLibro),name='respuestaLibro'),
    path('buscarLibro',login_required(buscarLibro),name='buscarLibro'),

    
    
]