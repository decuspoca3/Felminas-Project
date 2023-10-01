
from django.db import models
from django.db.models import Sum
from compra.models import Detallecompra
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
import re

# Create your models here.


def letras_validator(value):
    if not re.match("^[A-Za-zÁÉÍÓÚáéíóú ]+$", value):
        raise ValidationError('Este campo solo debe contener letras.')

class Producto(models.Model):
    nombre = models.CharField(max_length=45, verbose_name=_("Nombre"), validators=[letras_validator])
    descripcion = models.CharField(max_length=60, verbose_name=_("Descripcion"), validators=[letras_validator])
    marca = models.CharField(max_length=30, verbose_name=_("Marca"), validators=[letras_validator])
    precio = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_("Precio"))
    stock = models.IntegerField(verbose_name=_("Stock"))
    
    class Estado(models.TextChoices):
        ACTIVO = '1', _("Activo")
        INACTIVO = '0', _("Inactivo")
        CONDICIONADO = '2', _("Condicionado")

    estado = models.CharField(max_length=2, choices=Estado.choices, default=Estado.ACTIVO, verbose_name=_("Estado"))

    def __str__(self):
        return f"{self.nombre}"
    
    def precio_colombiano(self):
        formatted_price = "{:,.2f}".format(self.precio).replace(',', '#').replace('.', ',').replace('#', '.')
        return f"${formatted_price}"

    def actualizar_stock(self):
        total_comprado = Detallecompra.objects.filter(producto=self, compras__estado='1').aggregate(total=Sum('cantidad'))['total']
        total_vendido = self.detalleventa_set.filter(ventas__estado='1').aggregate(total=Sum('cantidad'))['total']
        stock_actual = self.stock + (total_comprado or 0) - (total_vendido or 0)
        self.stock = stock_actual
        self.save()
        return stock_actual
