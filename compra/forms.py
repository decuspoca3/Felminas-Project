from django.core.files.uploadedfile import UploadedFile
from django.forms import ModelForm, widgets
from compra.models import Ficha,Proyecto,Integrantes

from usuario.models import Usuario
from django import forms
from django.core.exceptions import ValidationError
from producto.models import Producto

#class UsuarioForm(ModelForm):
    
 #   class Meta:
  #      model = Usuario
  #      fields = "__all__"
   #     exclude=["estado",]
        # fields= ["nombre","apellido","documento","tipoDocumento"]
    #    widgets={
     #       'fecha_nacimiento': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d')
      #  }
        
   # def clean(self):
    #    cleaned_data = super().clean()
     #   documento = cleaned_data.get('documento')
      #  telefono_contacto = cleaned_data.get('telefono_contacto')
       # telefono_personal = cleaned_data.get('telefono_personal')
        #imagen = cleaned_data.get('imagen')

       # if documento and len(str(documento)) > 12:
        #    self.add_error('documento', "El documento no puede tener más de 12 dígitos")

        #if telefono_contacto and len(str(telefono_contacto)) > 10:
         #   self.add_error('telefono_contacto', "El teléfono no puede tener más de 10 dígitos")

        #if telefono_personal and len(str(telefono_personal)) > 10:
         #   self.add_error('telefono_personal', "El teléfono no puede tener más de 10 dígitos")

        #if imagen and isinstance(imagen, UploadedFile):
         #   ext = imagen.name.split('.')[-1].lower()
          #  if ext not in ['jpg', 'png']:
           #     self.add_error('imagen', "Solo se permiten archivos en formato PNG o JPG.")


   #     return cleaned_data
    
    #def __init__(self, *args, **kwargs):
     #   super(UsuarioForm, self).__init__(*args, **kwargs)
     #   self.fields["ficha"].queryset = Ficha.objects.filter(estado=Ficha.Estado.ACTIVO)

#class UsuarioUpdateForm(ModelForm):
    
 #   class Meta:
  #      model = Usuario
   #     fields = "__all__"
    #    exclude=["documento","rh","fecha_nacimiento"]
        
class FichaForm(ModelForm):
    
    class Meta:
        model = Ficha
        fields = "__all__"
        exclude=["estado",]
        widgets={
            'fecha_ingreso': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d'),
            'fecha_productiva': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d'),
            'fecha_final': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d')
            
        }

class FichaUpdateForm(ModelForm):
    
    class Meta:
        model = Ficha
        fields = "__all__"
        exclude=["numero","estado"]
    
class ProyectoForm(ModelForm):
    
    class Meta:
        model = Proyecto
        fields = "__all__"
        exclude=["estado","Empleado"]
    def __init__(self, *args, **kwargs):
        super(ProyectoForm, self).__init__(*args, **kwargs)

        self.fields["aprendiz"].queryset =Usuario.objects.filter(estado=Usuario.Estado.ACTIVO,rol=Usuario.Rol.PROVEEDOR)


class ProyectoUpdateForm(ModelForm):
    
    class Meta:
        model = Proyecto
        fields = "__all__"
        exclude=["fecha_creacion","estado"]
class IntegrantesForm(ModelForm):

    precio_str = forms.CharField(label="Precio Unitario", max_length=20)

    class Meta:
        model = Integrantes
        fields = "__all__"
        exclude=["estado","grupo","valortotal","Precio"]
        
    def clean_precio_str(self):
        precio_str = self.cleaned_data['precio_str']

        try:
            precio_decimal = round(float(precio_str.replace(",", "").replace(".", "").replace(" ", "")), 2)
            if precio_decimal < 0:
                raise ValidationError("El precio debe ser mayor o igual a cero.")
            return precio_decimal
        except (ValueError, TypeError):
            raise ValidationError("Asegúrese de ingresar un valor numérico válido.")
        
    def __init__(self, *args, **kwargs):
        super(IntegrantesForm, self).__init__(*args, **kwargs)
        self.fields["producto"].queryset =Producto.objects.filter(estado=Producto.Estado.ACTIVO)
