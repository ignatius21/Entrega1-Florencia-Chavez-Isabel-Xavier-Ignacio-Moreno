from django.urls import path
from AppEntrega.views import inicio,productos,nosotros,contacto,servicios,formulario,buscar


urlpatterns = [
    path('inicio',inicio,name='inicio'),
    path('productos',productos,name='productos'),
    path('nosotros',nosotros,name='nosotros'),
    path('contacto',contacto,name='contacto'),
    path('servicios',servicios,name='servicios'),
    path('formulario',formulario,name='formulario'),
    # path('buscarProducto',buscarProducto,name='buscarProducto'),
    path('buscar',buscar,name='buscar'),
    
]