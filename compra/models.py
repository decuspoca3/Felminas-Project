from django.db import models

from django.utils.translation import gettext_lazy as _
# Create your models here.
from usuario.models import Usuario
import uuid
from decimal import Decimal
import locale


class Compra(models.Model):
    fecha = models.DateField(verbose_name="Fecha", help_text="MM/DD/AAAA")
    numero_serie = models.CharField(max_length=100, unique=True, default=uuid.uuid4, editable=False)
    empleado_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='compras_realizadas',verbose_name="Empleado")
    proveedor_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='compras_recibidas',verbose_name="Proveedor")
    class Estado(models.TextChoices):
        ACTIVO = '1', _("Activo")
        INACTIVO = '0', _("Inactivo")

    estado = models.CharField(
        max_length=1, choices=Estado.choices,
        default=Estado.ACTIVO, verbose_name="Estado"
    )

    def __str__(self):
        return f"Id: {self.id}, Fecha: {self.fecha}, Empleado: {self.empleado_id}, Proveedor: {self.proveedor_id}  "

    class Meta:
        verbose_name_plural = "compras"

   
class Detallecompra(models.Model):
    cantidad = models.CharField(max_length=45, verbose_name="cantidad")
    valortotal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="valor total", null=True, blank=True)
    compras = models.ForeignKey("compra.Compra", on_delete=models.CASCADE, verbose_name="Compra")
    producto = models.ForeignKey("producto.Producto", on_delete=models.CASCADE, verbose_name="Producto")
    Precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio Unitario")

    class Estado(models.TextChoices):
        ACTIVO = '1', _("Activo")
        INACTIVO = '0', _("Inactivo")

    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

    def __str__(self):
        return f"Id : {self.id}, Compra: {self.compras} ,  Producto: {self.producto}"

    class Meta:
        verbose_name_plural = "detallecompras"
        
    def precio_colombiano(self):
        formatted_price = "{:,.2f}".format(self.Precio).replace(',', '#').replace('.', ',').replace('#', '.')
        return f"${formatted_price}"  
    
    def save(self, *args, **kwargs):
    # Asegurarse de que self.cantidad sea un Decimal
        cantidad_decimal = Decimal(self.cantidad) if self.cantidad else Decimal('0')
    
    # Asegurarse de que self.Precio sea un Decimal
        precio_decimal = self.Precio if isinstance(self.Precio, Decimal) else Decimal(str(self.Precio))
    
    # Calcula el valor total multiplicando la cantidad por el precio del producto
        self.valortotal = cantidad_decimal * precio_decimal
        super().save(*args, **kwargs)


    @property
    def valortotal_colombiano(self):
        locale.setlocale(locale.LC_ALL, "es_CO.UTF-8")
        formatted_valortotal = locale.currency(self.valortotal, grouping=True, symbol=False)
        return formatted_valortotal 