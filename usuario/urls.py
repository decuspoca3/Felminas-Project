from django.urls import path
from . import views
from usuario.views import usuario_listar, usuario_crear, usuario_modificar, usuario_eliminar 
from usuario.views import rol_listar, rol_crear, rol_modificar, rol_eliminar

urlpatterns = [
    path('usuario/', usuario_listar, name="usuario"),
    path('usuario/crear/', usuario_crear, name="usuario-crear"),
    path('usuario/modificar/<int:pk>/', usuario_modificar, name="usuario-modificar"),
    path('usuario/eliminar/<int:pk>/', usuario_eliminar, name="usuario-eliminar"),

    path('rol/', rol_listar, name="rol"),
    path('rol/crear/', rol_crear, name="rol-crear"),
    path('rol/modificar/<int:pk>/', rol_modificar, name="rol-modificar"),
    path('rol/eliminar/<int:pk>/', rol_eliminar, name="rol-eliminar"),


    path('hacer-backup/', views.hacer_backup, name='hacer_backup'), 
]
