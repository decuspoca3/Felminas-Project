
from django import forms
from django.forms import ModelForm
from producto.models import Producto
from django.core.exceptions import ValidationError
from django.contrib import messages

class ProductoForm(ModelForm):
    precio_str = forms.CharField(label="Precio", max_length=20)

    class Meta:
        model = Producto
        fields = "__all__"
        exclude = ['precio']

    def clean_precio_str(self):
        precio_str = self.cleaned_data['precio_str']
        precio_str = precio_str.replace(",", "")
        try:
            precio_decimal = float(precio_str)
            return precio_decimal
        except ValueError:
            raise forms.ValidationError("Asegúrese de ingresar un valor numérico válido.")
    
    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock < 0:
            self.add_error('stock', "El valor del stock debe ser un número positivo.")
        return stock

class ProductoUpdateForm(ModelForm):
    precio_edit = forms.CharField(
        label="Precio",
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
        
    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock < 0:
            self.add_error('stock', "El valor del stock debe ser un número positivo.")
        return stock
