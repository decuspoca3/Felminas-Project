from django.forms import ModelForm, widgets
from producto.models import Producto,Stock

class ProductoForm(ModelForm):

    class Meta:
        model = Producto
        fields = "__all__"

class ProductoUpdateForm(ModelForm):

    class Meta:
        model = Producto
        fields = "__all__"


class stockForm(ModelForm):

    class Meta:
        model = Stock
        fields = "__all__"

        widgets={
            'fecha': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d'),
        }

class stockUpdateForm(ModelForm):
    
    class Meta:
        model = Stock
        fields = "__all__"        