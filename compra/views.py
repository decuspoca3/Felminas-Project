from django.shortcuts import render, redirect, get_object_or_404
from compra.models import Ficha,Proyecto,Integrantes
from compra.forms import ProyectoForm, ProyectoUpdateForm
from compra.forms import IntegrantesForm
from compra.forms import FichaForm ,FichaUpdateForm
from django.contrib import messages
from django.urls import reverse, resolve
from PIL import Image
from django.urls import reverse
from . import urls
from django.core.paginator import Paginator, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from decimal import Decimal
import locale
from django.db import transaction
from django.db.models import F


    # """Esta funcion permite filtrar las urls
    # """
# def obtener_nombres_urls(modulo):
#     lista= urls.urlpatterns
#     names = list(set([url.name for url in lista if url.name is not None and url.name.startswith(modulo)]))
#     print(names)
#     return names
#     print(names)
#     return names
# # Create your views here.

@login_required
#def usuario_crear(request):
 #   titulo="Usuario"
    
 #   if request.method== 'POST':
    #    form= UsuarioForm(request.POST,request.FILES)
   #     if form.is_valid():
    #        usuario = form.save()
        #    if usuario.imagen:
                # Abre la imagen con Pillow
               # Abre la imagen original
          #      img = Image.open(usuario.imagen.path)

                # Redimensiona la imagen
           #     img = img.resize((500, 500))

                # Guarda la imagen redimensionada
      #          img.save(usuario.imagen.path)
            
       #     usuario.save()
 #           messages.success(request, 'El usuario se ha creado correctamente.')

     #       return redirect('usuarios')
     #   else:
     #       messages.error(request, 'Los datos del usuario tienen errores.')
  #  else:
  #      form= UsuarioForm()
  #  context={
 #       "titulo":titulo,
   #     "form":form
  #      }
  #  return render(request,"usuarios/usuarios/crear.html", context)

@login_required
#def usuario_listar(request, visualizar=1):
   # titulo="Usuario"
   # modulo="Usuarios"
    
    # urls_list=obtener_nombres_urls(modulo.lower())
    
  #  if visualizar==1:
   #     usuarios= Usuario.objects.filter(estado=visualizar)
   # else:
   #     usuarios= Usuario.objects.all()

  #  paginator = Paginator(usuarios, 3) # 3 usuarios por página
   # page_number = request.GET.get('page') # número de página actual
  #  try:
   #     usuarios = paginator.page(page_number)
   # except PageNotAnInteger:
        # Si el número de página no es un entero, mostrar la primera página.
     #   usuarios = paginator.page(1)
    #except EmptyPage:
        # Si el número de página está fuera de rango, mostrar la última página.
      #  usuarios = paginator.page(paginator.num_pages)
   # context={
        # "urls_list":urls_list,

     #   "titulo":titulo,
      #  "modulo":modulo,
      #  "usuarios":usuarios,
     #   "visualizar":visualizar
 #   }
   # return render(request,"usuarios/usuarios/listar.html", context)

@login_required
#def usuario_modificar(request,pk):
 #   titulo="Usuario"
  #  usuario= Usuario.objects.get(id=pk)
    
   # if request.method== 'POST':
    #    form= UsuarioUpdateForm(request.POST, instance=usuario)
     #   if form.is_valid():
    #        form.save()
   #         messages.success(request, 'El formulario se ha enviado correctamente.')
   #         return redirect('usuarios')
   # else:
    #    form= UsuarioUpdateForm(instance=usuario)
   # context={
  #      "titulo":titulo,
   #     "form":form
    #    }
  #  return render(request,"usuarios/usuarios/modificar.html", context)

#def usuario_eliminar(request,pk):
 #   usuario= Usuario.objects.filter(id=pk)
    
  #  usuario.update(
 #       estado="0"
 #   )
#    return redirect('usuarios')
   

@login_required
def ficha_crear(request):
    titulo="Ficha"
    if request.method== 'POST':
        form= FichaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fichas')
    else:
        form= FichaForm()
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"usuarios/fichas/crear.html", context)

@login_required
def ficha_listar(request):
    titulo="Ficha"
    modulo="Usuarios"
    fichas= Ficha.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "fichas":fichas
    }
    return render(request,"usuarios/fichas/listar.html", context)

@login_required
def ficha_modificar(request,pk):
    titulo="Fichas"
    
    ficha= Ficha.objects.get(id=pk)
    
    if request.method== 'POST':
        form= FichaUpdateForm(request.POST, instance=ficha)
        if form.is_valid():
            form.save()
            return redirect('fichas')
    else:
        form= FichaUpdateForm(instance=ficha)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"usuarios/fichas/modificar.html", context)

@login_required
def ficha_eliminar(request,pk):
    ficha= Ficha.objects.filter(id=pk)
    ficha.update(
        estado="0"
    )
    print(ficha[0].estado)
    return redirect('fichas')
   



def proyecto_listar(request):
    titulo="Compra"
    modulo="Usuarios"
    proyectos= Proyecto.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "proyectos":proyectos
    }
    return render(request,"proyectos/listar.html", context)




def proyecto_crear(request, pk=0):
    titulo = "Compras"
    modulo = "Usuarios"
    proyecto = Proyecto.objects.filter(id=pk)
    integrantes = Integrantes.objects.filter(grupo_id=pk)
    total_valores = integrantes.aggregate(Sum('valortotal'))['valortotal__sum'] or Decimal(0.0)
     
    locale.setlocale(locale.LC_ALL, "es_CO.UTF-8")
    total_valores_colombiano = locale.currency(total_valores, grouping=True, symbol=False)
    
    # para el form de creación del grupo
    if request.method == 'POST' and 'form-grupo' in request.POST:
        form_proyecto = ProyectoForm(request.POST)
        if form_proyecto.is_valid():
            # Crear una instancia de Proyecto pero no guardarla en la base de datos todavía
            proyecto_nuevo = form_proyecto.save(commit=False)

            # Asignar el usuario autenticado (Empleado) al campo Empleado del proyecto
            proyecto_nuevo.Empleado = request.user

            # Guardar el proyecto en la base de datos
            proyecto_nuevo.save()

            return redirect('compras-crear', proyecto_nuevo.id)
        else:
            messages.danger(request, 'Error al crear el grupo.')

    else:
        form_proyecto = ProyectoForm()

    # para el form de agregar aprendiz al grupo
    if request.method == 'POST' and 'form-integrante' in request.POST:
        form_integrante = IntegrantesForm(request.POST)
        if form_integrante.is_valid():
            integrante_data = form_integrante.cleaned_data
            producto_id = integrante_data['producto'].id

            # Verificar si el producto ya existe en el grupo
            existing_integrante = Integrantes.objects.filter(grupo_id=pk, producto_id=producto_id).first()

            if existing_integrante:
                # Si el producto ya existe, solo actualiza la cantidad
                existing_integrante.cantidad += integrante_data['cantidad']
                existing_integrante.save()
                messages.success(request, 'Se actualizó la cantidad del producto.')
            else:
                # Si el producto no existe, crea un nuevo registro
                precio_decimal = form_integrante.cleaned_data['precio_str']
                integrante = form_integrante.save(commit=False)
                integrante.grupo_id = pk
                integrante.Precio = precio_decimal
                integrante.save()
                messages.success(request, 'El aprendiz se agregó correctamente.')

            return redirect('compras-crear', pk)
        else:
            messages.success(request, 'Error al agregar el aprendiz.')

    else:
        form_integrante = IntegrantesForm()

    context = {
        "form_integrante": form_integrante,
        "form_proyecto": form_proyecto,
        "titulo": titulo,
        "modulo": modulo,
        "proyecto": proyecto,
        "integrantes": integrantes,
        'total_valores': total_valores,
        'total_valores_colombiano': total_valores_colombiano,
    }
    return render(request, "proyectos/crear.html", context)

 
def proyecto_modificar(request,pk):
    titulo="Proyectos"
    
    proyecto= Proyecto.objects.get(id=pk)
    
    if request.method== 'POST':
        form= ProyectoUpdateForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('compras')
    else:
        form= ProyectoUpdateForm(instance=proyecto)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"proyectos/modificar.html", context)


def proyecto_eliminar(request, pk):
    proyecto = Proyecto.objects.filter(id=pk)
    integrantes = Integrantes.objects.filter(grupo_id=pk)

    if integrantes:
        try:
            with transaction.atomic():
                for integrante in integrantes:
                    producto = integrante.producto
                    producto.stock = F('stock') + integrante.cantidad
                    producto.save()
            proyecto.update(estado="0")  # Cambiar el estado del proyecto a "0"
            return redirect('compras')
        except Exception as e:
            messages.error(request, f'Error al actualizar el stock: {str(e)}')
    else:
        messages.error(request, 'No puedes finalizar la Compra sin un detalle compra. Agrega al menos uno antes de finalizarlo.')

    return redirect('compras')



def integrante_eliminar(request,pk):
    integrante = get_object_or_404(Integrantes, id=pk)
    id_proy=integrante.grupo.id
    integrante.delete()
    return redirect('compras-crear',id_proy)



def proyecto_final(request,pk):
    titulo="Compra"
    modulo="Usuarios"
    proyectos= Proyecto.objects.filter(id=pk)
    integrantes = Integrantes.objects.filter(grupo_id=pk)
    total_valores = integrantes.aggregate(Sum('valortotal'))['valortotal__sum'] or Decimal(0.0)
 
    locale.setlocale(locale.LC_ALL, "es_CO.UTF-8")
    total_valores_colombiano = locale.currency(total_valores, grouping=True, symbol=False)
    context={
        "titulo":titulo,
        "modulo":modulo,
        "proyectos":proyectos,
        "integrantes": integrantes,
        'total_valores': total_valores,
        'total_valores_colombiano': total_valores_colombiano,

    }
    return render(request,"proyectos/listar_Compra.html", context)