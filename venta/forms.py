from django.forms import ModelForm, widgets
from venta.models import venta ,Detalleventa

class VentaForm(ModelForm):

    class Meta:
        model = venta
        fields = "__all__"
        
        widgets={
            'fecha': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d'),
        }

class VentaUpdateForm(ModelForm):
    
    class Meta:
        model = venta
        fields = "__all__"
        exclude=["estado"]


class DetalleventaForm(ModelForm):

    class Meta:
        model = Detalleventa
        fields = "__all__"

        widgets={
            'fecha': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d'),
        }

class DetalleventaUpdateForm(ModelForm):
    
    class Meta:
        model = Detalleventa
        fields = "__all__"      