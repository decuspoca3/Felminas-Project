from django.db import models

from django.utils.translation import gettext_lazy as _
# Create your models here.
from usuario.models import Usuario
class Compra(models.Model):
    fecha = models.DateField(verbose_name="Fecha", help_text="MM/DD/AAAA")

    class Estado(models.TextChoices):
        ACTIVO = '1', _("Activo")
        INACTIVO = '0', _("Inactivo")

    estado = models.CharField(
        max_length=1, choices=Estado.choices,
        default=Estado.ACTIVO, verbose_name="Estado"
    )

    def __str__(self):
        return f"Id: {self.id}, Fecha: {self.fecha}"

    class Meta:
        verbose_name_plural = "compras"

   
class Detallecompra(models.Model):
    precio = models.CharField(max_length=45, verbose_name="precio")
    cantidad = models.CharField(max_length=45, verbose_name="cantidad")
    valortotal = models.CharField(max_length=45, verbose_name="valor total")
    compras = models.ForeignKey("compra.Compra", on_delete=models.CASCADE, verbose_name="Compra")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuario")
    producto = models.ForeignKey("producto.Producto", on_delete=models.CASCADE, verbose_name="Producto")
    
    class Estado(models.TextChoices):
        ACTIVO = '1', _("Activo")
        INACTIVO = '0', _("Inactivo")

    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

    def __str__(self):
        return f"Id : {self.id}, Compra: {self.compras} , Usuario: {self.usuario} , Producto: {self.producto}"

    class Meta:
        verbose_name_plural = "detallecompras"

