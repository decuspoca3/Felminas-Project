from django.forms import ModelForm, widgets
from compra.models import Compra ,Detallecompra
from django import forms
from django.core.exceptions import ValidationError

class CompraForm(ModelForm):

    class Meta:
        model = Compra
        fields = "__all__"
        exclude = ["estado"]


        widgets={
            'fecha': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d'),
        }

class CompraUpdateForm(ModelForm):
    
    class Meta:
        model = Compra 
        fields = "__all__"
        exclude = ["estado"]

class DetallecompraForm(ModelForm):
    precio_str = forms.CharField(label="Precio Unitario", max_length=20)

    class Meta:
        model = Detallecompra
        exclude = ['valortotal', 'estado', 'Precio']
        fields = "__all__"

        widgets = {
            'fecha': widgets.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

    def clean_precio_str(self):
        precio_str = self.cleaned_data['precio_str']
        precio_str = precio_str.replace(",", "").replace(".", "")  # Remover comas y puntos
        try:
            precio_decimal = float(precio_str)
            return precio_decimal
        except ValueError:
            raise forms.ValidationError("Asegúrese de ingresar un valor numérico válido.")


class DetallecompraUpdateForm(ModelForm):
    precio_edit = forms.CharField(
        label="Precio Unitario",
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'Ejemplo: 980.000'})
    )

    class Meta:
        model = Detallecompra
        fields = "__all__"
        exclude = ['valortotal', 'estado', 'Precio']

    def clean_precio_edit(self):
        precio_edit = self.cleaned_data['precio_edit']
        precio_edit = precio_edit.replace(",", "").replace(".", "").replace(" ", "")  # Remover comas, puntos y espacios
        try:
            precio_decimal = round(float(precio_edit), 2)
            if precio_decimal < 0:
                raise ValidationError("El precio debe ser mayor o igual a cero.")
            return precio_decimal
        except (ValueError, TypeError):
            raise ValidationError("Precio no válido. Asegúrese de que no hayan más de 2 decimales.")
