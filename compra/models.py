from django.db import models

from django.utils.translation import gettext_lazy as _
# Create your models here.
from usuario.models import Usuario
import uuid
from decimal import Decimal



class Compra(models.Model):
    fecha = models.DateField(verbose_name="Fecha", help_text="MM/DD/AAAA")
    numero_serie = models.CharField(max_length=100, unique=True, default=uuid.uuid4, editable=False)
    empleado_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='compras_realizadas',verbose_name="Empleado")
    proveedor_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='compras_recibidas',verbose_name="Proveedor")
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    class Estado(models.TextChoices):
        ACTIVO = '1', _("Activo")
        INACTIVO = '0', _("Inactivo")

    estado = models.CharField(
        max_length=1, choices=Estado.choices,
        default=Estado.ACTIVO, verbose_name="Estado"
    )

    def __str__(self):
        return f"Id: {self.id}, Fecha: {self.fecha}, Empleado: {self.empleado_id}, Proveedor: {self.proveedor_id} "

    class Meta:
        verbose_name_plural = "compras"

   
class Detallecompra(models.Model):
    cantidad = models.CharField(max_length=45, verbose_name="cantidad")
    valortotal = models.CharField(max_length=45, verbose_name="valor total")
    compras = models.ForeignKey("compra.Compra", on_delete=models.CASCADE, verbose_name="Compra")
    producto = models.ForeignKey("producto.Producto", on_delete=models.CASCADE, verbose_name="Producto")

    class Estado(models.TextChoices):
        ACTIVO = '1', _("Activo")
        INACTIVO = '0', _("Inactivo")

    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

    def __str__(self):
        return f"Id : {self.id}, Compra: {self.compras} , Usuario: {self.usuario} , Producto: {self.producto}"

    class Meta:
        verbose_name_plural = "detallecompras"
        
        
    def save(self, *args, **kwargs):
        # Calcula el valor total multiplicando la cantidad por el precio del producto
        self.valortotal = Decimal(self.cantidad) * self.producto.precio

        super().save(*args, **kwargs)