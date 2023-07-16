import os
from django.db import connection
from dbbackup.management.commands.dbbackup import Command as DbBackupCommand
from django.http import HttpResponse
from django.shortcuts import render, redirect
from usuario.models import Usuario, Rol
from usuario.forms import UsuarioForm, UsuarioUpdateForm, RolForm, RolUpdateForm
from django.http import JsonResponse

def hacer_backup(request):
    # Ruta donde deseas guardar el archivo de backup (asegúrate de que la carpeta "backups" exista)
    backup_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'base', 'backups')
    backup_file = f'{backup_dir}/nombre_del_archivo.bak'

    # Lógica para realizar el backup aquí
    verbosity_level = 1  # Establece un valor entero para verbosity, p. ej. 1
    DbBackupCommand().handle(filename=backup_file, verbosity=verbosity_level)

    return redirect('usuario')

def usuario_crear(request):
    titulo="Usuario"
    if request.method== 'POST':
        form= UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuario')
    else:
        form= UsuarioForm()
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request,"usuario/crear.html", context )

def usuario_listar(request):
    titulo="Usuario"
    usuarios= Usuario.objects.all()
    context={
        "titulo":titulo,
        "usuarios":usuarios
    }
    return render(request,"usuario/listar.html", context)

def usuario_modificar(request,pk):
    titulo="Usuario"
    usuario= Usuario.objects.get(id=pk)

    if request.method=='POST':
        form= UsuarioUpdateForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
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

def rol_crear(request):
    titulo="Rol"
    if request.method== 'POST':
        form= RolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rol')
    else:
        form= RolForm()
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request,"rol/crear.html", context )




def rol_listar(request):
    titulo="Rol"
    roles= Rol.objects.all()
    context={
        "titulo":titulo,
        "roles":roles
    }
    return render(request,"rol/listar.html", context)

def rol_modificar(request,pk):
    titulo="Usuario"
    rol= Rol.objects.get(id=pk)

    if request.method=='POST':
        form= RolUpdateForm(request.POST, instance=rol)
        if form.is_valid():
            form.save()
            return redirect('rol')
    else:
        form= RolUpdateForm(instance=rol)
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request,"rol/modificar.html", context)

def rol_eliminar(request,pk):
    rol= Rol.objects.filter(id=pk)
    rol.update(
        estado="0"
    )
    return redirect('rol')

