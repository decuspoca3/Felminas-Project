from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.forms import PasswordResetForm  # Agrega esta línea de importación
from django.shortcuts import render, redirect
from cuenta.models import Cuenta
from cuenta.forms import  UsuarioUpdateForm
from cuenta.forms import UsuarioCreationForm
from django.urls import reverse
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.decorators import login_required
from usuario.models import Usuario

@login_required()
def cuenta_crear(request):
    titulo = "Cuenta"
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Guardar el usuario recién creado

            # Obtener el token para restablecimiento de contraseña
            token = default_token_generator.make_token(user)

            # Construir la URL de restablecimiento de contraseña
            protocol = 'http'
            domain = request.META['HTTP_HOST']
            reset_url = reverse('password_reset_confirm', kwargs={'uidb64':  urlsafe_base64_encode(force_bytes(user.id)), 'token': token})

            # Construir el mensaje de correo
            email_content = f"Hola {user.username},\n\n"
            email_content += "Has solicitado restablecer tu contraseña. Haz clic en el siguiente enlace:\n\n"
            email_content += f"{protocol}://{domain}{reset_url}\n\n"
            email_content += "Si no solicitaste este restablecimiento de contraseña, ignora este correo.\n\n"
            email_content += "Gracias,\nEl equipo de TuNombreDeSitio"

            # Enviar el correo
            send_mail(
                'Restablecimiento de contraseña',
                email_content,
                'noreply@example.com',
                [user.email],
                fail_silently=False,
            )

            return redirect('cuenta')
    else:
        form = UsuarioCreationForm() 
        usuarios_activos = Usuario.objects.filter(estado='1',rol=Usuario.Rol.EMPLEADO)  # Obtener solo los usuarios activos
        form.fields['empleado_usuario'].queryset = usuarios_activos
    context = {
        "titulo": titulo,
        "form": form
    }
    return render(request, "cuenta/crear.html", context)

@login_required
def cuenta_listar(request):
    titulo="Cuenta"
    cuentas= Cuenta.objects.all()
    context={
        "titulo":titulo,
        "cuentas":cuentas,
        "user": request.user
    
    }
    return render(request,"cuenta/listar.html", context)
@login_required()
def cuenta_modificar(request,pk):
    titulo="Cuenta"
    cuenta= Cuenta.objects.get(id=pk)

    if request.method=='POST':
        form= UsuarioUpdateForm(request.POST, instance=cuenta)
        if form.is_valid():
            form.save()
            return redirect('cuenta')
    else:
        form= UsuarioUpdateForm(instance=cuenta)
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request,"cuenta/modificar.html", context)
@login_required()
def cuenta_eliminar(request,pk): 
    cuenta= Cuenta.objects.filter(id=pk)
    cuenta.delete()
    return redirect('cuenta')

