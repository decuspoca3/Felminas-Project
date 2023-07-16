from django.urls import path

from producto.views import producto_listar, producto_crear, producto_modificar, producto_eliminar,stock_crear,stock_eliminar,stock_modificar,stock_listar

urlpatterns = [
    path('producto/', producto_listar, name="producto"),
    path('producto/crear/', producto_crear, name="producto-crear"),
    path('producto/modificar/<int:pk>/', producto_modificar, name="producto-modificar"),
    path('producto/eliminar/<int:pk>/', producto_eliminar, name="producto-eliminar"),

    path('stock/', stock_listar, name="stock" ),
    path('stock/crear/', stock_crear, name="stock_crear" ),
    path('stock/modificar/<int:pk>/', stock_modificar, name="stock_modificar" ),
    path('stock/eliminar/<int:pk>/', stock_eliminar, name="stock_eliminar" ),    
]