from django.urls import path
from AppEntrega.views import inicio,productos,nosotros,contacto,servicios

urlpatterns = [
    path('',inicio,name='inicio'),
    path('productos',productos,name='productos'),
    path('nosotros',nosotros,name='nosotros'),
    path('contacto',contacto,name='contacto'),
    path('servicios',servicios,name='servicios'),
    
]