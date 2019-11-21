from django.urls import path
from .views import crearAutor

urlpatterns = [
    #path recibe: ruta url / función de la vista / nombre de la ruta
    path('crear_autor/',crearAutor,name='crear_autor')
]
