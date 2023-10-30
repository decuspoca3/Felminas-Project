from django.urls import path

#from compra.views import usuario_listar, usuario_crear, usuario_modificar, usuario_eliminar
from venta.views import venta_listar, venta_crear, venta_modificar, venta_eliminar
from venta.views import detalleventa_eliminar,  venta_final




urlpatterns = [
  
    path('venta/', venta_listar, name="ventas" ),

    path('venta/crear/', venta_crear, name="ventas-crear" ),
    path('venta/gestionar/<int:pk>/', venta_crear, name="ventas-crear" ),

    path('venta/modificar/<int:pk>/', venta_modificar, name="ventas-modificar" ),
    path('venta/eliminar/<int:pk>/', venta_eliminar, name="ventas-eliminar" ),

    path('venta/detalleventa/eliminar/<int:pk>/', detalleventa_eliminar, name="detalleventa-eliminar" ),
    path('venta/final/<int:pk>/', venta_final, name="venta-final" ),

]
