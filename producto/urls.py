from django.urls import path

from producto.views import producto_listar, producto_crear, producto_modificar, producto_eliminar

urlpatterns = [
    path('producto/', producto_listar, name="producto"),
    path('producto/crear/', producto_crear, name="producto-crear"),
    path('producto/modificar/<int:pk>/', producto_modificar, name="producto-modificar"),
    path('producto/eliminar/<int:pk>/', producto_eliminar, name="producto-eliminar"),


]