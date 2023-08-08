from django.urls import path
from .views import Register
urlpatterns = [
    path('accounts/', Register, name="Registrarse" ),

]


from django.urls import path
from .views import Register
urlpatterns = [
    path('accounts/', Register, name="Registrarse" ),

]