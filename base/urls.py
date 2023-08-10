"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from base.views import principal, logout_user

from django.conf import settings
from django.conf.urls.static import static
# para la gestion de login y contraseña
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetDoneView ,PasswordResetView,PasswordResetCompleteView, PasswordResetConfirmView ,LoginView ,LogoutView
urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='inicio'),
    path('logout/', logout_user, name="logout"),
    path('reiniciar/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reiniciar/enviar/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reiniciar/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reiniciar/completo/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('admin/', admin.site.urls),
    path('inicio/', principal, name="index"),
    path('usuario/', include('usuario.urls')),
    path('producto/', include('producto.urls')),
    path('venta/', include('venta.urls')),
    path('compra/', include('compra.urls')),

    path('google-auth/', views.google_auth, name='google_auth'),
    path('google-auth-callback/', views.google_auth_callback, name='google_auth_callback'),
]