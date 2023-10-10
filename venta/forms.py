from django.core.files.uploadedfile import UploadedFile
from django.forms import ModelForm
from venta.models import Venta,Detalleventa
from cuenta.models import Cuenta
from django import forms

class VentaForm(ModelForm):
    
    class Meta:
        model = Venta
        fields = "__all__"
        exclude=["estado","Empleado"]
    def __init__(self, *args, **kwargs):
        super(VentaForm, self).__init__(*args, **kwargs)
        self.fields["aprendiz"].queryset =Cuenta.objects.filter(estado=Cuenta.Estado.ACTIVO,rol=Cuenta.Rol.ADMIN)


class VentaUpdateForm(ModelForm):
    
    class Meta:
        model = Venta
        fields = "__all__"
        exclude=["fecha_creacion","estado"]

class DetalleventaForm(ModelForm):

    precio_str = forms.CharField(label="Precio Unitario", max_length=20)

    class Meta:
        model = Detalleventa
        fields = "__all__"
        exclude=["estado","grupo","valortotal","Precio"]
        
    def clean_precio_str(self):
        precio_str = self.cleaned_data['precio_str']
        precio_str = precio_str.replace(",", "").replace(".", "")  # Remover comas y puntos
        try:
            precio_decimal = float(precio_str)
            return precio_decimal
        except ValueError:
            raise forms.ValidationError("Asegúrese de ingresar un valor numérico válido.")
