from django.shortcuts import render

# Create your views here.
#request es el parametro que va obtener de la interacción del usuario
def Home(request):
    return render(request,'libro/index.html')