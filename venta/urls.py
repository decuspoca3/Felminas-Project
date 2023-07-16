from django.urls import path

from venta.views import venta_listar, venta_crear, venta_modificar, venta_eliminar
from venta.views import detalleventa_eliminar, detalleventa_listar, detalleventa_modificar, detalleventa_crear
urlpatterns = [
    path('venta/', venta_listar, name="venta" ),
    path('venta/crear/', venta_crear, name="venta_crear" ),
    path('venta/modificar/<int:pk>/', venta_modificar, name="venta_modificar" ),
    path('venta/eliminar/<int:pk>/', venta_eliminar, name="venta_eliminar" ),  
   
    path('detalleventa/', detalleventa_listar, name="detalleventa" ),
    path('detalleventa/crear/', detalleventa_crear, name="detalleventa_crear" ),
    path('detalleventa/modificar/<int:pk>/', detalleventa_modificar, name="detalleventa_modificar" ),
    path('detalleventa/eliminar/<int:pk>/', detalleventa_eliminar, name="detalleventa_eliminar" ),      
]