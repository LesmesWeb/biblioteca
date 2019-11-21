from django import forms
#cuando se encuentra el archivo dentro de la carpeta se llama con el . 
from .models import Autor

#sistema de plantillas automatico del formulario
class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre','apellidos','nacionalidad','descripcion']