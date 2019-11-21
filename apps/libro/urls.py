from django.urls import path
from .views import Home

urlpatterns = [
    #path recibe: ruta url / función de la vista / nombre de la ruta
    path('',Home,name='index')
]
