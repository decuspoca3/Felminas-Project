from django.urls import path
from . import views
from usuario.views import usuario_listar, usuario_crear, usuario_modificar, usuario_eliminar 
from usuario.views import salario_listar, salario_crear, salario_modificar, salario_eliminar

urlpatterns = [
    path('usuario/', usuario_listar, name="usuario"),
    path('usuario/crear/', usuario_crear, name="usuario-crear"),
    path('usuario/modificar/<int:pk>/', usuario_modificar, name="usuario-modificar"),
    path('usuario/eliminar/<int:pk>/', usuario_eliminar, name="usuario-eliminar"),

    path('salario/', salario_listar, name="salario"),
    path('salario/crear/', salario_crear, name="salario-crear"),
    path('salario/modificar/<int:pk>/', salario_modificar, name="salario-modificar"),
    path('salario/eliminar/<int:pk>/', salario_eliminar, name="salario-eliminar"),

    path('hacer-backup/', views.hacer_backup, name='hacer_backup'), 
]

