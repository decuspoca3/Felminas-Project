from django.db import models
from django.db.models import Sum
from compra.models import Detallecompra
from django.utils.translation import gettext_lazy as _

class Producto(models.Model):
    nombre = models.CharField(max_length=45, verbose_name=_("Nombre"))
    descripcion = models.CharField(max_length=60, verbose_name=_("Descripcion"))
    marca = models.CharField(max_length=30, verbose_name=_("Marca"))
    precio = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_("Precio"))
    stock = models.IntegerField(verbose_name=_("Stock"))
    
    class Estado(models.TextChoices):
        ACTIVO = '1', _("Activo")
        INACTIVO = '0', _("Inactivo")
        CONDICIONADO = '2', _("Condicionado")

    estado = models.CharField(max_length=2, choices=Estado.choices, default=Estado.ACTIVO, verbose_name=_("Estado"))

    def __str__(self):
        return f"Producto: {self.nombre} ,Stock: {self.stock} "
    
    def precio_colombiano(self):
     formatted_price = "${:,.0f}".format(self.precio)  # Sin decimales y sin coma separadora
     return formatted_price

    
    
    
    def actualizar_stock(self):
        # Obtener la suma total de la cantidad comprada en Detallecompra
        total_comprado = Detallecompra.objects.filter(producto=self, compras__estado='1').aggregate(total=Sum('cantidad'))['total']

        # Obtener la suma total de la cantidad vendida en Detalleventa
        total_vendido = self.detalleventa_set.filter(ventas__estado='1').aggregate(total=Sum('cantidad'))['total']

        # Calcular el stock actual (stock + compras - ventas)
        stock_actual = self.stock + (total_comprado or 0) - (total_vendido or 0)

        # Actualizar el valor de stock en el modelo
        self.stock = stock_actual
        self.save()

        return stock_actual