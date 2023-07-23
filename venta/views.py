from django.shortcuts import render, redirect
from venta.models import venta,Detalleventa
from venta.forms import VentaForm, VentaUpdateForm ,DetalleventaForm,DetalleventaUpdateForm
from producto.models import Producto 
from usuario.models import Usuario
def venta_crear(request):
    titulo="Venta"
    if request.method=='POST':
        form= VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('venta')
    else:
        form= VentaForm()
        usuarios_activos = Usuario.objects.filter(estado='1', rol=Usuario.Rol.EMPLEADO)  # Obtener solo los usuarios activos
        form.fields['usuario'].queryset = usuarios_activos
        productos_activos = Producto.objects.filter(estado='1')  # Obtener solo los productos activos
        form.fields['producto'].queryset = productos_activos
        
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request,"venta/crear.html",context)

def venta_listar(request):
    titulo="venta"
    Venta= venta.objects.all()
    context={
        "titulo":titulo,
        "ventas":Venta
    }
    return render(request,"venta/listar.html", context)

def venta_modificar(request,pk):
    titulo="venta"
    Venta= venta.objects.get(id=pk)

    if request.method=='POST':
        form= VentaUpdateForm(request.POST, instance=Venta)
        if form.is_valid():
            form.save()
            return redirect('venta')
    else:
        form= VentaUpdateForm(instance=Venta)
        usuarios_activos = Usuario.objects.filter(estado='1')  # Obtener solo los usuarios activos
        form.fields['usuario'].queryset = usuarios_activos
        productos_activos = Producto.objects.filter(estado='1')  # Obtener solo los productos activos
        form.fields['producto'].queryset = productos_activos
                
        context={
            "titulo":titulo,
            "form":form
                }
        return render(request,"venta/modificar.html", context)

def venta_eliminar(request,pk):
    Venta= venta.objects.filter(id=pk)
    Venta.update(
        estado="0"
    )
    return redirect('venta')




def detalleventa_crear(request):
    titulo="Detalleventa"
    if request.method=='POST':
        form= DetalleventaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detalleventa')
    else:
        form= DetalleventaForm()
        ventas_activos = venta.objects.filter(estado='1')  
        form.fields['ventas'].queryset =  ventas_activos
       
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request,"detalleventa/crear.html",context)

def detalleventa_listar(request):
    titulo="Detalleventa"
    detalleventa= Detalleventa.objects.all()
    context={
        "titulo":titulo,
        "detalleventas":detalleventa
    }
    return render(request,"detalleventa/listar.html", context)

def detalleventa_modificar(request,pk):
    titulo="Detalleventa"
    detalleventa= Detalleventa.objects.get(id=pk)

    if request.method=='POST':
        form= DetalleventaUpdateForm(request.POST, instance=detalleventa)
        if form.is_valid():
            form.save()
            return redirect('detalleventa')
    else:
        form= DetalleventaUpdateForm(instance=detalleventa)
        ventas_activos = venta.objects.filter(estado='1')  
        form.fields['ventas'].queryset =  ventas_activos
        stocks_activos = Stock.objects.filter(estado='1') 
        form.fields['stocks'].queryset = stocks_activos
                
        context={
            "titulo":titulo,
            "form":form
                }
        return render(request,"detalleventa/modificar.html", context)

def detalleventa_eliminar(request,pk):
    detalleventa= Detalleventa.objects.filter(id=pk)
    detalleventa.update(
        estado="0"
    )
    return redirect('detalleventa')