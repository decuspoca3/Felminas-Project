from django.forms import ModelForm, widgets
from producto.models import Producto

class ProductoForm(ModelForm):

    class Meta:
        model = Producto
        fields = "__all__"

class ProductoUpdateForm(ModelForm):

    class Meta:
        model = Producto
        fields = "__all__"

