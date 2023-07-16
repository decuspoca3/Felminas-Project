from django.shortcuts import render, redirect
from producto.models import Producto ,Stock
from producto.forms import ProductoForm, ProductoUpdateForm,stockForm,stockUpdateForm
# Create your views here.
from compra.models import Detallecompra
def producto_crear(request):
    titulo="Producto"
    if request.method== 'POST':
        form= ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto')
    else:
        form= ProductoForm()
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request,"producto/crear.html", context )

def producto_listar(request):
    titulo="Producto"
    productos= Producto.objects.all()
    context={
        "titulo":titulo,
        "productos":productos
    }
    return render(request,"producto/listar.html", context)

def producto_modificar(request,pk):
    titulo="Producto"
    producto= Producto.objects.get(id=pk)

    if request.method=='POST':
        form= ProductoUpdateForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto')
    else:
        form= ProductoUpdateForm(instance=producto)
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request,"producto/modificar.html", context)

def producto_eliminar(request,pk):
    producto= Producto.objects.filter(id=pk)
    producto.update(
        estado="0"
    )
    return redirect('producto')

def stock_crear(request):
    titulo="Stock"
    if request.method=='POST':
        form= stockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock')   
    else:
        form= stockForm()
        detalle_compra_activos = Detallecompra.objects.filter(estado='1')  
        form.fields['detalle_compra'].queryset =  detalle_compra_activos
    context={
        "titulo":titulo,
        "form":form
    }       
    return render(request,"stock/crear.html",context)

def stock_listar(request):
    titulo="Stock"
    stock= Stock.objects.all()
    context={
        "titulo":titulo,
        "stocks":stock
    }
    return render(request,"stock/listar.html", context)

def stock_modificar(request,pk):
    titulo="Stock"
    stock= Stock.objects.get(id=pk)

    if request.method=='POST':
        form= stockUpdateForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            return redirect('stock')
    else:
        form= stockUpdateForm(instance=stock)
        detalle_compra_activos = Detallecompra.objects.filter(estado='1')  # Obtener solo los usuarios activos
        form.fields['detalle_compra'].queryset =  detalle_compra_activos
                
        context={
            "titulo":titulo,
            "form":form
                }
        return render(request,"stock/modificar.html", context)

def stock_eliminar(request,pk):
    stock= Stock.objects.filter(id=pk)
    stock.update(
        estado="0"
    )
    return redirect('stock') 