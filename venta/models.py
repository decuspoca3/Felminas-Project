from django.db import models
from django.utils.translation import gettext_lazy as _
from cuenta.models import Cuenta
from  producto.models import Producto
import uuid
from decimal import Decimal
import locale
from django.db.models import Sum 
from django.core.exceptions import ValidationError

from usuario.models import Usuario

def validate_positive(value):
        if value < 1:
            raise ValidationError("La cantidad debe ser un número positivo.")
        


class Venta(models.Model):
    nombre= models.CharField(max_length=100, unique=True, default=uuid.uuid4, editable=False)
    aprendiz= models.ForeignKey(Usuario,verbose_name="Cliente",related_name="Cliente", on_delete=models.CASCADE)
    Empleado= models.ForeignKey(Cuenta,verbose_name="Empleado", on_delete=models.CASCADE)

    
    
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTIVO='0',_("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")
    fecha_creacion = models.DateField(auto_now=True, verbose_name="Fecha de Creación")
    def __str__(self):
        return f"{self.aprendiz}"



class Detalleventa(models.Model):
    cantidad=models.IntegerField( verbose_name="cantidad", validators=[validate_positive])
    grupo=models.ForeignKey(Venta,verbose_name="Grupo", on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto")

    valortotal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="valor total", null=True, blank=True)

    
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTIVO='0',_("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")
    

    def precio_colombiano(self):
        formatted_price = "{:,.2f}".format(self.Precio).replace(',', '#').replace('.', ',').replace('#', '.')
        return f"${formatted_price}"  
    
    def save(self, *args, **kwargs):
    # Asegurarse de que self.cantidad sea un Decimal
        cantidad_decimal = Decimal(self.cantidad) if self.cantidad else Decimal('0')
    

    def actualizar_stock_producto(self):
        if self.estado == Detalleventa.Estado.ACTIVO:
            producto = self.producto
            producto.stock -= self.cantidad
            producto.save()
            
    def save(self, *args, **kwargs):
        self.valortotal_calculado = self.cantidad * self.producto.precio
        self.valortotal = self.valortotal_calculado
        super().save(*args, **kwargs)

    def calcular_total_valores():
       total = Detalleventa.objects.aggregate(Sum('valortotal'))['valortotal__sum']
       return total or Decimal(0.0)

    @property
    def valortotal_colombiano(self):
        locale.setlocale(locale.LC_ALL, "es_CO.UTF-8")
        formatted_valortotal = locale.currency(self.valortotal, grouping=True, symbol=False)
        return formatted_valortotal 
