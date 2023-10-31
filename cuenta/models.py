from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _
from usuario.models import Usuario

class Cuenta(AbstractUser):
    groups = models.ManyToManyField(Group, blank=True, related_name="usuarios")
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='usuarios')
    empleado_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Rol(models.TextChoices):
        ADMIN = 'Admin', _("Admin")
        EMPLEADO = 'Empleado', _("Empleado")
        

    rol = models.CharField(max_length=10, choices=Rol.choices, verbose_name="Rol")

    class Estado(models.TextChoices):
        ACTIVO = '1', _("Activo")
        INACTIVO = '0', _("Inactivo")
        
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    
    class Meta:
        verbose_name_plural = "Cuentas"

   



