from django.shortcuts import render, redirect
# libreria para capturar errores
from django.core.exceptions import ObjectDoesNotExist
from .forms import AutorForm
from .models import Autor
# Create your views here.
# request es el parametro que va obtener de la interacción del usuario


def Home(request):
    return render(request, 'index.html')


def crearAutor(request):
    if request.method == 'POST':
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect('index')
    else:
        autor_form = AutorForm()

    return render(request, 'libro/crear_autor.html', {'autor_form': autor_form})

# Vistas basadas en funciones


def listarAutor(request):
    autores = Autor.objects.all()
    return render(request, 'libro/listar_autor.html', {'autores': autores})


def editarAutor(request, id):
    # declaramos el formulario para que muestre el error de try
    autor_form = None
    error = None
    # se creara un try cash con el proposito de solucionar el error del get cuando no existe el ID
    try:
        # con get solo traemos el unico dato que encuentre de la base de datos
        autor = Autor.objects.get(id=id)
        if request.method == 'GET':
            autor_form = AutorForm(instance=autor)
        else:
            autor_form = AutorForm(request.POST, instance=autor)
            if autor_form.is_valid():
                autor_form.save()
            return redirect('index')
    # Para capturar la excepción se debe importar la libreria ObjectDoesNotExist
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'libro/crear_autor.html', {'autor_form': autor_form, 'error': error})
