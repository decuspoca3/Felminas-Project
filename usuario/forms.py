from django.forms import ModelForm, widgets
from usuario.models import Usuario, Salario

class UsuarioForm(ModelForm):

    class Meta:
        model = Usuario
        fields = "__all__"
        exclude = ["estado"]

        widgets={
            'fecha_nacimiento': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d')
        }

        

class UsuarioUpdateForm(ModelForm):

    class Meta:
        model = Usuario
        fields = "__all__"
        exclude = ["documento","estado"]


class SalarioForm(ModelForm):

    class Meta:
        model = Salario
        fields = "__all__"
        exclude = ["estado"]

        widgets={
            'fecha': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d')
        }

class SalarioUpdateForm(ModelForm):

    class Meta:
        model = Salario
        fields = "__all__"
        exclude = ["estado"]

