from django.urls import path
from AppEntrega import views

urlpatterns = [
    path('', views.inicio),
    path('productos', views.productos),
    path('nosotros', views.nosotros),
    path('contacto', views.contacto),
    path('servicios', views.servicios),
    
]