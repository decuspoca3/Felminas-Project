from django.core.files.uploadedfile import UploadedFile
from django.forms import ModelForm
from venta.models import Venta,Detalleventa
from usuario.models import Usuario
from django import forms
from producto.models import Producto
class VentaForm(ModelForm):


    class Meta:
        model = Venta
        fields = "__all__"
        exclude=["estado","Empleado"]
   
    def __init__(self, *args, **kwargs):
        super(VentaForm, self).__init__(*args, **kwargs)
        self.fields["aprendiz"].queryset =Usuario.objects.filter(estado=Usuario.Estado.ACTIVO,rol=Usuario.Rol.CLIENTE)
   
   
class VentaUpdateForm(ModelForm):
    
    class Meta:
        model = Venta
        fields = "__all__"
        exclude=["fecha_creacion","estado"]

class DetalleventaForm(ModelForm):

    class Meta:
        model = Detalleventa
        fields = "__all__"
        exclude=["estado","grupo","valortotal"]

    def __init__(self, *args, **kwargs):
        super(DetalleventaForm, self).__init__(*args, **kwargs)
        self.fields["producto"].queryset =Producto.objects.filter(estado=Producto.Estado.ACTIVO)
    
