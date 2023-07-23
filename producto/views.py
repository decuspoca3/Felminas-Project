from django.shortcuts import render, redirect
from producto.models import Producto 
from producto.forms import ProductoForm, ProductoUpdateForm
# Create your views here.

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
