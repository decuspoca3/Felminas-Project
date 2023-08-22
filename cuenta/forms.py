from django.forms import ModelForm, widgets
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Cuenta
from .models import Cuenta, Usuario

class UsuarioCreationForm(UserCreationForm):
    rol = forms.ChoiceField(choices=Cuenta.Rol.choices, required=True)
    empleado_usuario = forms.ModelChoiceField(queryset=Usuario.objects.filter(rol=Usuario.Rol.EMPLEADO), required=True)


    class Meta:
        model = Cuenta
        fields = ('username', 'email','empleado_usuario', 'password1', 'password2' ,'rol', 'is_superuser')
        exclude = [
             'estado'
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields.pop('password2')
    def clean_email(self):
        email = self.cleaned_data['email']
        if Cuenta.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está registrado.")
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Contraseña'})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user



                
class UsuarioUpdateForm(ModelForm):

    class Meta:
        model = Cuenta
        fields = "__all__"
        exclude = [
            "ultimo_inicio_de_sesion", "nombre", "apellidos", "es_staff", "activo", "fecha_de_alta", "groups", "user_permissions",
        ]

