from django.urls import path
from compra.views import compra_listar, compra_crear, compra_modificar, compra_eliminar
from compra.views import detallecompra_crear,detallecompra_listar,detallecompra_eliminar,detallecompra_modificar

urlpatterns = [
    path('compra/', compra_listar, name="compra" ),
    path('compra/crear/', compra_crear, name="compra_crear" ),
    path('compra/modificar/<int:pk>/', compra_modificar, name="compra_modificar" ),
    path('compra/eliminar/<int:pk>/', compra_eliminar, name="compra_eliminar" ),

    path('detallecompra/', detallecompra_listar, name="detallecompra" ),
    path('detallecompra/crear/', detallecompra_crear, name="detallecompra_crear" ),
    path('detallecompra/modificar/<int:pk>/', detallecompra_modificar, name="detallecompra_modificar" ),
    path('detallecompra/eliminar/<int:pk>/', detallecompra_eliminar, name="detallecompra_eliminar" ),    


]