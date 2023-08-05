from django import forms
from django.forms import ModelForm
from producto.models import Producto
from django.utils.translation import gettext_lazy as _
from decimal import Decimal  # Agrega esta línea para importar la clase Decimal
from django.core.exceptions import ValidationError

class ProductoForm(ModelForm):
    precio_str = forms.CharField(label="Precio", max_length=20)

    class Meta:
        model = Producto
        fields = "__all__"
        exclude = ['precio']  # Excluye el campo 'precio' del formulario


    def clean_precio_str(self):
        precio_str = self.cleaned_data['precio_str']
        precio_str = precio_str.replace(",", "").replace(".", "")  # Remover comas y puntos
        try:
            precio_decimal = Decimal(precio_str) / 100  # Convertir a formato decimal (2 decimales)
            return precio_decimal
        except DecimalException:  # Reemplaza DecimalException con la excepción adecuada
            raise forms.ValidationError("Asegúrese de que no haya más de 2 decimales.")
        
        
        
        
class ProductoUpdateForm(ModelForm):
    precio_edit = forms.CharField(
        label="Precio Edición",
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'Ejemplo: 980.000'})
    )

    class Meta:
        model = Producto
        exclude = ['precio']
        fields = "__all__"

    def clean_precio_edit(self):
        precio_edit = self.cleaned_data['precio_edit']
        try:
            precio_decimal = round(float(precio_edit.replace(",", "").replace(".", "").replace(" ", "")), 2)
            if precio_decimal < 0:
                raise ValidationError("El precio debe ser mayor o igual a cero.")
            return precio_decimal
        except (ValueError, TypeError):
            raise ValidationError("Precio no válido. Asegúrese de que no hayan más de 2 decimales.")