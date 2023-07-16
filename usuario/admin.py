from django.contrib import admin
from usuario.models import Usuario, Rol, Usuario_Rol


admin.site.register(Usuario)
admin.site.register(Rol)
admin.site.register(Usuario_Rol)



