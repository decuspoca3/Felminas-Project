from django.shortcuts import render, redirect
from venta.models import venta, Detalleventa
from venta.forms import VentaForm, VentaUpdateForm, DetalleventaForm, DetalleventaUpdateForm
from producto.models import Producto 
from usuario.models import Usuario
from django.contrib import messages
import os
from dbbackup.management.commands.dbbackup import Command as DbBackupCommand
from dbbackup.management.commands.dbrestore import Command as DbRestoreCommand
from django.core.management import call_command
from django.http import JsonResponse
from decimal import Decimal
from django.contrib.auth.decorators import login_required



def hacer_backup_venta(request):
    backup_file = 'base/backups/backup_venta.json'
    call_command('dumpdata', 'venta', 'detalleventa', 'producto', 'usuario', output=backup_file)
    return JsonResponse({'success': True, 'message': 'Copia de seguridad realizada correctamente.'})

def hacer_restore_venta(request):
    backup_file = 'base/backups/backup_venta.json'
    call_command('loaddata', backup_file)
    return JsonResponse({'success': True, 'message': 'Restauración de copia de seguridad realizada correctamente.'})







def vender_producto(request, producto_id):
    producto = Producto.objects.get(pk=producto_id)

    if request.method == 'POST':
        cantidad_vendida = int(request.POST['cantidad'])
        if cantidad_vendida > 0 and cantidad_vendida <= producto.stock:
            # Realizar la venta
            Venta = venta.objects.create(
                numero_serie='SERIAL_NUMBER',  # Coloca un número de serie adecuado
                cliente_id=request.user,  # Suponiendo que estás utilizando el modelo de usuario de Django
                empleado_id=request.user,  # Suponiendo que estás utilizando el modelo de usuario de Django
                fecha='FECHA_DE_VENTA',  # Coloca la fecha actual de la venta
                monto='MONTO_DE_VENTA'  # Coloca el monto total de la venta
            )
            
            # Crear el detalle de venta
            Detalleventa.objects.create(
                cantidad=cantidad_vendida,
                venta=venta,
                producto=producto,
                valor_total='VALOR_TOTAL'  # Coloca el valor total del detalle de venta
            )

            # Actualizar el stock del producto
            producto.stock -= cantidad_vendida
            producto.save()

            return redirect('venta_exitosa')
        else:
            error_message = "Cantidad inválida o insuficiente stock"
            return render(request, 'venta_fallida.html', {'error_message': error_message})

    return render(request, 'form_venta.html', {'producto': producto})

@login_required()
def venta_crear(request):
    titulo = "Venta"
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Venta creado exitosamente.')

        return redirect('detalleventa_crear')
    else:
        form = VentaForm()
        usuarios_activos = Usuario.objects.filter(estado='1', rol=Usuario.Rol.CLIENTE)  # Obtener solo los usuarios activos
        form.fields['cliente_id'].queryset = usuarios_activos
        usuarios_activos = Usuario.objects.filter(estado='1', rol=Usuario.Rol.EMPLEADO)  # Obtener solo los usuarios activos
        form.fields['empleado_id'].queryset = usuarios_activos

    context = {
        "titulo": titulo,
        "form": form
    }
    return render(request, "venta/crear.html", context)

@login_required()
def venta_listar(request):
    titulo = "venta"
    ventas = venta.objects.all()
    context = {
        "titulo": titulo,
        "ventas": ventas
    }
    return render(request, "venta/listar.html", context)

@login_required()
def venta_modificar(request, pk):
    titulo = "venta"
    venta_obj = venta.objects.get(id=pk)

    if request.method == 'POST':
        form = VentaUpdateForm(request.POST, instance=venta_obj)
        if form.is_valid():
            form.save()
        messages.success(request, 'Venta modificado exitosamente.')

        return redirect('venta')
    else:
        form = VentaUpdateForm(instance=venta_obj)
        usuarios_activos = Usuario.objects.filter(estado='1', rol=Usuario.Rol.CLIENTE)  # Obtener solo los usuarios activos
        form.fields['cliente_id'].queryset = usuarios_activos
        usuarios_activos = Usuario.objects.filter(estado='1', rol=Usuario.Rol.EMPLEADO)  # Obtener solo los usuarios activos
        form.fields['empleado_id'].queryset = usuarios_activos
        
        context = {
            "titulo": titulo,
            "form": form
        }
        return render(request, "venta/modificar.html", context)

def venta_eliminar(request, pk):
    venta_obj = venta.objects.get(id=pk)
    venta_obj.estado = venta.Estado.INACTIVA
    venta_obj.save()
    return redirect('venta')


@login_required()
def detalleventa_crear(request):
    titulo = "Detalleventa"
    if request.method == 'POST':
        form = DetalleventaForm(request.POST)
        if form.is_valid():
            detalleventa = form.save(commit=False)  # No guardar el modelo aún, solo crea la instancia del objeto
            producto = detalleventa.producto
            cantidad_vendida = detalleventa.cantidad

            if cantidad_vendida <= producto.stock:  # Verificar si la cantidad vendida es menor o igual al stock
                detalleventa.actualizar_stock_producto()  # Actualizar el stock del producto
                detalleventa.save()  # Ahora sí, guardar la venta

                messages.success(request, 'Detalle de venta creado exitosamente.')  # Mensaje de éxito
                return redirect('detalleventa')
            else:
                # Mostrar un mensaje de error si la cantidad vendida supera el stock
                messages.error(request, f"No hay suficiente stock disponible. Stock actual: {producto.stock}")
        else:
            messages.error(request, "Formulario inválido. Verifica los datos ingresados.")
    else:
        form = DetalleventaForm()
        ventas_activas = venta.objects.filter(estado='1')  
        form.fields['ventas'].queryset = ventas_activas
        productos_activos = Producto.objects.filter(estado='1')  # Obtener solo los productos activos
        form.fields['producto'].queryset = productos_activos
        
    context = {
        "titulo": titulo,
        "form": form
    }
    return render(request, "detalleventa/crear.html", context)




@login_required()
def detalleventa_listar(request):
    titulo = "Detalleventa"
    detalleventa = Detalleventa.objects.all()
    context = {
        "titulo": titulo,
        "detalleventas": detalleventa
    }
    return render(request, "detalleventa/listar.html", context)

@login_required()
def detalleventa_modificar(request, pk):
    titulo = "Detalleventa"
    detalleventa = Detalleventa.objects.get(id=pk)

    if request.method == 'POST':
        form = DetalleventaUpdateForm(request.POST, instance=detalleventa)
        if form.is_valid():
            form.save()
        messages.success(request, 'Detalle de venta modificado exitosamente.')  # Mensaje de éxito

        return redirect('detalleventa')
    else:
        form = DetalleventaUpdateForm(instance=detalleventa)
        ventas_activas = venta.objects.filter(estado='1')  
        form.fields['ventas'].queryset = ventas_activas
        productos_activos = Producto.objects.filter(estado='1')  # Obtener solo los productos activos
        form.fields['producto'].queryset = productos_activos
                
        context = {
            "titulo": titulo,
            "form": form
        }
        return render(request, "detalleventa/modificar.html", context)

def detalleventa_eliminar(request, pk):
    detalleventa = Detalleventa.objects.get(id=pk)
    detalleventa.estado = Detalleventa.Estado.INACTIVO
    detalleventa.save()
    return redirect('detalleventa')
