from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
import re
from django.core.validators import RegexValidator

def letras_validator(value):
    if not re.match("^[A-Za-zÁÉÍÓÚáéíóú ]+$", value):
        raise ValidationError('Este campo solo debe contener letras.')
    
def numeros_validator(value):
    if not re.match("^[0-9]+$", value):
        raise ValidationError('Este campo solo debe contener números.')

def unique_documento_validator(value):
    if Usuario.objects.filter(documento=value).exists():
           raise ValidationError('Este documento ya está registrado.') 
       
def unique_correo(value):
    if Usuario.objects.filter(correo=value).exists():
           raise ValidationError('Este correo ya está registrado.')  
    
class Usuario(models.Model):
    primer_nombre = models.CharField(max_length=45, verbose_name=_("Primer Nombre"), validators=[letras_validator])
    segundo_nombre = models.CharField(max_length=45, verbose_name=_("Segundo Nombre"), validators=[letras_validator])
    primer_apellido = models.CharField(max_length=45, verbose_name=_("Primer Apellido"), validators=[letras_validator])
    segundo_apellido = models.CharField(max_length=45, verbose_name=_("Segundo Apellido"), validators=[letras_validator])

    class Tipo_Documento(models.TextChoices):
        CEDULA = 'CC', _("Cédula Ciudadania")
        TARJETA = 'TI', _("Tarjeta de Identidad")
        CEDULA_EXTRANJERIA = 'CE', _("Cédula de Extranjería")

    tipo_documento = models.CharField(max_length=2, choices=Tipo_Documento.choices, verbose_name="Tipo de Documento")
    documento = models.CharField(max_length=20, verbose_name="Documento",validators=[numeros_validator, unique_documento_validator])

    telefono_contacto = models.CharField(max_length=10, verbose_name="Teléfono de contacto",validators=[numeros_validator])
    telefono_personal = models.CharField(max_length=10, verbose_name="Teléfono personal",validators=[numeros_validator]) 

    class Rol(models.TextChoices):
        EMPLEADO = 'Empleado', _("Empleado")
        PROVEEDOR = 'Proveedor', _("Proveedor")
        CLIENTE = 'Cliente', _("Cliente")

    rol = models.CharField(max_length=10, choices=Rol.choices, verbose_name="Rol")

    correo = models.CharField(max_length=40, verbose_name="Correo Electrónico",validators=[unique_correo])

    class Estado(models.TextChoices):
        ACTIVO = '1', _("Activo")
        INACTIVO = '0', _("Inactivo")
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    
   
   
    def __str__(self):
        return "%s %s" % (self.primer_nombre, self.primer_apellido)

    class Meta:
        verbose_name_plural = "Usuarios"

class Salario(models.Model):

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Empleado")

    class Nivel(models.TextChoices):
        NIVEL1 = '1', _("Nivel 1")
        NIVEL2 = '2', _("Nivel 2")
        NIVEL3 = '3', _("Nivel 3")
        NIVEL4 = '4', _("Nivel 4")

    nivel = models.CharField(max_length=1, choices=Nivel.choices, verbose_name="Nivel de Salario")
    fecha = models.DateField(verbose_name="Fecha", help_text="DD/MM/AAAA")

    class Estado(models.TextChoices):
        ACTIVO = '1', _("Activo")
        INACTIVO = '0', _("Inactivo")

    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

    def __str__(self):
        return f"Salario Nivel {self.nivel} - Fecha: {self.fecha}"

    class Meta:
        verbose_name_plural = "Salarios"








    

