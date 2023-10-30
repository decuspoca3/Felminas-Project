from django.urls import path

#from compra.views import usuario_listar, usuario_crear, usuario_modificar, usuario_eliminar
from compra.views import ficha_listar, ficha_crear, ficha_modificar, ficha_eliminar
from compra.views import proyecto_listar, proyecto_crear, proyecto_modificar, proyecto_eliminar
from compra.views import integrante_eliminar,  proyecto_final




urlpatterns = [
    #path('usuario/<int:visualizar>/', usuario_listar, name="usuarios" ),
    #path('usuario/', usuario_listar, name="usuarios" ),

    #path('usuario/crear/', usuario_crear, name="usuarios-crear" ),
    #path('usuario/modificar/<int:pk>/', usuario_modificar, name="usuarios-modificar" ),
    #path('usuario/eliminar/<int:pk>/', usuario_eliminar, name="usuarios-eliminar" ),
    
    path('ficha/', ficha_listar, name="fichas" ),
    path('ficha/crear/', ficha_crear, name="fichas-crear" ),
    path('ficha/modificar/<int:pk>/', ficha_modificar, name="fichas-modificar" ),
    path('ficha/eliminar/<int:pk>/', ficha_eliminar, name="fichas-eliminar" ),

    path('proyecto/', proyecto_listar, name="compras" ),

    path('proyecto/crear/', proyecto_crear, name="compras-crear" ),
    path('proyecto/gestionar/<int:pk>/', proyecto_crear, name="compras-crear" ),

    path('proyecto/modificar/<int:pk>/', proyecto_modificar, name="compras-modificar" ),
    path('proyecto/eliminar/<int:pk>/', proyecto_eliminar, name="compras-eliminar" ),

    path('proyecto/integrante/eliminar/<int:pk>/', integrante_eliminar, name="integrante-eliminar" ),
    path('proyecto/final/<int:pk>/', proyecto_final, name="compras-final" ),

]
