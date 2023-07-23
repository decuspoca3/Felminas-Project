from django.db import models
from django.utils.translation import gettext_lazy as _
from producto.models import Producto
from usuario.models import Usuario


# Create your models here.
class venta(models.Model):
    fecha= models.DateField(verbose_name="Fecha", help_text="MM/DD/AAAA")
    usuario = models.ForeignKey(Usuario , on_delete=models.CASCADE, verbose_name="Usuario")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto")
      
    class Estado(models.TextChoices):
        ACTIVA='1',_("Activa")
        INACTIVA='0',_("Inactiva")
            
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVA,verbose_name="Estado")
    def __str__(self):
        return f"Id Venta: {self.id}, Fecha: {self.fecha} , Usuario: {self.usuario}, Producto: {self.producto}"       
    class Meta:
        verbose_name_plural= "ventas"
        
     
@classmethod
def obtener_ventas_empleados(cls):
    return cls.objects.filter(usuario__rol=Usuario.Rol.EMPLEADO)

@classmethod
def obtener_ventas_clientes(cls):
    return cls.objects.filter(usuario__rol=Usuario.Rol.CLIENTE)
        
class Detalleventa(models.Model):
    valortotal= models.CharField(max_length=45, verbose_name="valor total")
    ventas = models.ForeignKey("venta.venta", on_delete=models.CASCADE, verbose_name="Venta")
    
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTIVO='0',_("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")

    class Meta:
        verbose_name_plural = "detalleventas" 
