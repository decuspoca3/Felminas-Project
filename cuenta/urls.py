from django.urls import path

from cuenta.views import cuenta_listar, cuenta_crear, cuenta_modificar, cuenta_eliminar

urlpatterns = [
    path('cuenta/', cuenta_listar, name="cuenta"),
    path('cuenta/crear/', cuenta_crear, name="cuenta-crear"),
    path('cuenta/modificar/<int:pk>/', cuenta_modificar, name="cuenta-modificar"),
    path('cuenta/eliminar/<int:pk>/', cuenta_eliminar, name="cuenta-eliminar"),


]
