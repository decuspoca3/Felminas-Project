from django.forms import ModelForm, widgets
from compra.models import Compra ,Detallecompra

class CompraForm(ModelForm):

    class Meta:
        model = Compra
        fields = "__all__"

        widgets={
            'fecha': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d'),
        }

class CompraUpdateForm(ModelForm):
    
    class Meta:
        model = Compra 
        fields = "__all__"
        exclude = ["estado"]

class DetallecompraForm(ModelForm):

    class Meta:
        model = Detallecompra
        fields = "__all__"

        widgets={
            'fecha': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d'),
        }

class DetallecompraUpdateForm(ModelForm):
    
    class Meta:
        model = Detallecompra
        fields = "__all__"      
