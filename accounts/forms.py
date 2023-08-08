from django import forms
from django.contrib.auth.models import User,Group
from django.contrib.auth.forms import UserCreationForm
from .models import Register

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Usuario', min_length=5, max_length=150, widget=forms.TextInput(attrs={'class': 'custom-input', 'placeholder':'Nombre de Usuario'}))
    email = forms.EmailField(label='Correo', widget=forms.EmailInput(attrs={'class': 'custom-input','placeholder':'Correo Electronico'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'custom-input','placeholder':'Contraseña'}))
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(attrs={'class': 'custom-input','placeholder':'Confirmar Contraseña'}))
    activo = forms.BooleanField(initial=False, widget=forms.HiddenInput, required=False)
    group = forms.ModelChoiceField(queryset=Group.objects.all(), label='Rol', required=False )

    class Meta(UserCreationForm.Meta):
        # Asegurarse de que el modelo sea User
        model = User
        fields = UserCreationForm.Meta.fields + ('group',)  # Agregar el nuevo campo al formulario

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username=username)
        if new.count():
            raise forms.ValidationError("El Usuario ya Existe")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El Correo ya Existe")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las Contraseñas no Coinciden")
        return password2

    def save(self, commit=True):
        username = self.cleaned_data['username']  # Obtener el nombre de usuario
        email = self.cleaned_data['email']
        password = self.cleaned_data['password1']
        user = User.objects.create_user(username=username, email=email, password=password)
        register = Register.objects.create(usuario=username, activo=False)  # Pasar el nombre de usuario
        register.save()