from django.db import models
from django.utils.translation import gettext_lazy as _
from producto.models import Producto
from usuario.models import Usuario
from django.db.models import Sum
import uuid


class venta(models.Model):
    numero_serie = models.CharField(max_length=100, unique=True, default=uuid.uuid4, editable=False)
    cliente_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='ventas_realizadas',verbose_name=_("Cliente"))
    empleado_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='ventas_atendidas',verbose_name=_("Empleado")) 
    fecha = models.DateField(verbose_name="Fecha", help_text="MM/DD/AAAA")
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    class Estado(models.TextChoices):
        ACTIVA = '1', _("Activa")
        INACTIVA = '0', _("Inactiva")
            
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVA, verbose_name="Estado")

    def __str__(self):
        return f"Id Venta: {self.id}, Fecha: {self.fecha}, Empleado: {self.empleado_id}, Cliente: {self.cliente_id}"
  

   

    class Meta:
        verbose_name_plural = "ventas"

class Detalleventa(models.Model):
    cantidad = models.IntegerField()
    ventas = models.ForeignKey("venta.venta", on_delete=models.CASCADE, verbose_name="Venta")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto")
    valortotal = models.CharField(max_length=10, verbose_name="valor total")

    class Estado(models.TextChoices):
        ACTIVO = '1', _("Activo")
        INACTIVO = '0', _("Inactivo")

    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

    class Meta:
        verbose_name_plural = "detalleventas" 

    def actualizar_stock_producto(self):
        if self.estado == Detalleventa.Estado.ACTIVO:
            producto = self.producto
            producto.stock -= self.cantidad
            producto.save()