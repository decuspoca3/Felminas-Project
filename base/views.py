from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
@login_required()


def principal(request):
    titulo="Inicio"
    context={
        "titulo":titulo
    }
    return render(request, "index.html",context)

def logout_user(request):
    logout(request)
    return redirect('inicio')
def google_auth(request):
    # Implementa aquí la lógica para redireccionar al usuario a la página de autorización de Google
    auth_url = f"https://accounts.google.com/o/oauth2/auth?client_id={settings.GOOGLE_CLIENT_ID}&redirect_uri={settings.GOOGLE_REDIRECT_URI}&response_type=code&scope=email%20profile"
    return redirect(auth_url)

def google_auth_callback(request):
    # Implementa aquí la lógica para manejar la respuesta de Google después de la autorización
    # y obtener los tokens de acceso necesarios para autenticar al usuario
    code = request.GET.get('code')
    # Realiza la solicitud para obtener los tokens de acceso utilizando el código recibido de Google
    # y guarda los tokens en la sesión del usuario
    # Luego, redirige al usuario a la página principal de tu aplicación
    return redirect('inicio')
