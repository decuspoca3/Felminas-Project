from django.shortcuts import render, redirect
from compra.models import Compra ,Detallecompra
from compra.forms import CompraForm, CompraUpdateForm ,DetallecompraForm,DetallecompraUpdateForm
from producto.models import Producto
from usuario.models import Usuario
def compra_crear(request):
    titulo="Compra"
    if request.method=='POST':
        form= CompraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detallecompra_crear')   
    else:
        form= CompraForm()
        
    context={
        "titulo":titulo,
        "form":form
    }       
    return render(request,"compra/crear.html",context)

def compra_listar(request):
    titulo="Compra"
    compra= Compra.objects.all()
    context={
        "titulo":titulo,
        "compras":compra
    }
    return render(request,"compra/listar.html", context)

def compra_modificar(request,pk):
    titulo="Compra"
    compra= Compra.objects.get(id=pk)

    if request.method=='POST':
        form= CompraUpdateForm(request.POST, instance=compra)
        if form.is_valid():
            form.save()
            return redirect('compra')
    else:
        form= CompraUpdateForm(instance=compra)
                
        context={
            "titulo":titulo,
            "form":form
                }
        return render(request,"compra/modificar.html", context)

def compra_eliminar(request,pk):
    compra= Compra.objects.filter(id=pk)
    compra.update(
        estado="0"
    )
    return redirect('compra')




def detallecompra_crear(request):
    titulo="Detallecompra"
    if request.method=='POST':
        form= DetallecompraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detallecompra')
    else:
        form= DetallecompraForm()
        usuarios_activos = Usuario.objects.filter(estado='1',rol=Usuario.Rol.CLIENTE)  # Obtener solo los usuarios activos
        form.fields['usuario'].queryset = usuarios_activos
        productos_activos = Producto.objects.filter(estado='1')  # Obtener solo los productos activos
        form.fields['producto'].queryset = productos_activos
        compra_activos = Compra.objects.filter(estado='1') 
        form.fields['compras'].queryset = compra_activos
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request,"detallecompra/crear.html",context)

def detallecompra_listar(request):
    titulo="Detallecompra"
    detallecompra= Detallecompra.objects.all()
    context={
        "titulo":titulo,
        "detallecompras":detallecompra
    }
    return render(request,"detallecompra/listar.html", context)

def detallecompra_modificar(request,pk):
    titulo="Detallecompra"
    detallecompra= Detallecompra.objects.get(id=pk)

    if request.method=='POST':
        form= DetallecompraUpdateForm(request.POST, instance=detallecompra)
        if form.is_valid():
            form.save()
            return redirect('detallecompra')
    else:
        form= DetallecompraUpdateForm(instance=detallecompra)
        usuarios_activos = Usuario.objects.filter(estado='1')  # Obtener solo los usuarios activos
        form.fields['usuario'].queryset = usuarios_activos
        productos_activos = Producto.objects.filter(estado='1')  # Obtener solo los productos activos
        form.fields['producto'].queryset = productos_activos
        compra_activos = Compra.objects.filter(estado='1') 
        form.fields['compras'].queryset = compra_activos       
        context={
            "titulo":titulo,
            "form":form
                }
        return render(request,"detallecompra/modificar.html", context)

def detallecompra_eliminar(request,pk):
    detallecompra= Detallecompra.objects.filter(id=pk)
    detallecompra.update(
        estado="0"
    )
    return redirect('detallecompra')