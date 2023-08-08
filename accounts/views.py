from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import Register
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            group = form.cleaned_data['group']  # Obtener el grupo seleccionado en el formulario
            messages.success(request, 'La persona se creo correctamente.')
            if group:
                user.groups.add(group)  # Agregar el usuario al grupo seleccionado
            return redirect('inicio')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/crear.html', {'form': form})


def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')