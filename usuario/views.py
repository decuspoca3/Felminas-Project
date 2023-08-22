import os
from django.db import connection
from dbbackup.management.commands.dbbackup import Command as DbBackupCommand
from django.http import HttpResponse
from django.shortcuts import render, redirect
from usuario.models import Usuario, Salario
from usuario.forms import UsuarioForm, UsuarioUpdateForm, SalarioForm, SalarioUpdateForm
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError


def hacer_backup(request):
    # Ruta donde deseas guardar el archivo de backup (asegúrate de que la carpeta "backups" exista)
    backup_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'base', 'backups')
    backup_file = f'{backup_dir}/nombre_del_archivo.bak'

    # Lógica para realizar el backup aquí
    verbosity_level = 1  # Establece un valor entero para verbosity, p. ej. 1
    DbBackupCommand().handle(filename=backup_file, verbosity=verbosity_level)

    return redirect('usuario')


@login_required()
def usuario_crear(request):
    titulo = "Usuario"
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Usuario creado exitosamente.')
                return redirect('usuario')
            except IntegrityError as e:
                messages.error(request, 'Error al crear el usuario: {}'.format(str(e)))

    else:
        form = UsuarioForm()

    context = {
        "titulo": titulo,
        "form": form
    }
    return render(request, "usuario/crear.html", context)


@login_required()
def usuario_listar(request):
    titulo="Usuario"
    usuarios= Usuario.objects.all()
    context={
        "titulo":titulo,
        "usuarios":usuarios
    }
    return render(request,"usuario/listar.html", context)

@login_required()
def usuario_modificar(request,pk):
    titulo="Usuario"
    usuario= Usuario.objects.get(id=pk)

    if request.method=='POST':
        form= UsuarioUpdateForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
        messages.success(request, 'Usuario modificado exitosamente.')

        return redirect('usuario')
    else:
        form= UsuarioUpdateForm(instance=usuario)
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request,"usuario/modificar.html", context)

def usuario_eliminar(request,pk):
    usuario= Usuario.objects.filter(id=pk)
    usuario.update(
        estado="0"
    )
    return redirect('usuario')

@login_required()
def salario_crear(request):
    titulo = "Salario"
    if request.method == 'POST':
        form = SalarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Salario creado exitosamente.')
            return redirect('salario')
    else:
        form = SalarioForm()
        usuarios_activos = Usuario.objects.filter(estado='1', rol=Usuario.Rol.EMPLEADO)  # Obtener solo los usuarios activos
        form.fields['usuario'].queryset = usuarios_activos
    context = {
        "titulo": titulo,
        "form": form
    }
    return render(request, "salario/crear.html", context)


@login_required()
def salario_listar(request):
    titulo = "Salario"
    salarios = Salario.objects.all()
    context = {
        "titulo": titulo,
        "salarios": salarios
    }
    return render(request, "salario/listar.html", context)

@login_required()
def salario_modificar(request, pk):
    titulo = "Salario"
    salario = Salario.objects.get(id=pk)

    if request.method == 'POST':
        form = SalarioUpdateForm(request.POST, instance=salario)
        if form.is_valid():
            form.save()
        messages.success(request, 'Salario modificado exitosamente.')

        return redirect('salario')
    else:
        form = SalarioUpdateForm(instance=salario)
        usuarios_activos = Usuario.objects.filter(estado='1', rol=Usuario.Rol.EMPLEADO)  # Obtener solo los usuarios activos
        form.fields['usuario'].queryset = usuarios_activos
    context = {
        "titulo": titulo,
        "form": form
    }
    return render(request, "salario/modificar.html", context)

@login_required()
def salario_eliminar(request, pk):
    salario = Salario.objects.filter(id=pk)
    salario.update(estado="0")
    return redirect('salario')

