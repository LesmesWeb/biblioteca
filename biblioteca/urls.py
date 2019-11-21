"""biblioteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include #con include se pueden añadir archivos de las apps
from apps.libro.views import Home
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('libro/',include('libro.urls'))
    #se debe crear el archivo url en el  app y con esta linea lo enrutamos
    path('libro/',include(('apps.libro.urls','libro'))),
    path('home/', Home, name='index'),
]
