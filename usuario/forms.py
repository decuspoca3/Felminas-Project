from django.forms import ModelForm, widgets
from usuario.models import Usuario, Rol

class UsuarioForm(ModelForm):

    class Meta:
        model = Usuario
        fields = "__all__"

        widgets={
            'fecha_nacimiento': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d')
        }

class UsuarioUpdateForm(ModelForm):

    class Meta:
        model = Usuario
        fields = "__all__"
        exclude = ["documento","fecha_nacimiento"]

class RolForm(ModelForm):

    class Meta:
        model = Rol
        fields = "__all__"
        widgets={
            'fecha': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d')
        }

class RolUpdateForm(ModelForm):

    class Meta:
        model = Rol
        fields = "__all__"
