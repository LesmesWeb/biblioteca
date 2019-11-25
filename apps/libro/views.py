from django.shortcuts import render, redirect
# libreria para capturar errores
from django.core.exceptions import ObjectDoesNotExist
from .forms import AutorForm
from .models import Autor
# Create your views here.
# request es el parametro que va obtener de la interacción del usuario


def Home(request):
    return render(request, 'index.html')

#Crear el registro de un Autor desde el forms.py requiere que en el template sean los mismos nombres
def crearAutor(request):
    if request.method == 'POST':
        print(request.POST) # la salida es: <QueryDict: {'csrfmiddlewaretoken': ['#####'], 'nombre': ['1'], 'apellidos': ['2'], 'nacionalidad': ['3'], 'descripcion': ['4']}>
        autor_form = AutorForm(request.POST) #recibe los valores en el mismo orden en el que esten en el archivos forms.py
        if autor_form.is_valid(): #django guarda con valid los datos en cleaned_data
            nom = autor_form.cleaned_data['nombre']
            print("nom ",nom)
            autor_form.save()
            return redirect('libro:listar_autor')
            #return redirect('index')
    else:
        autor_form = AutorForm()

    return render(request, 'libro/crear_autor.html',{'autor_form': autor_form})

#Crear el registro de un Autor recibiendo los datos desde el template y los nombres pueden cambiar
#def crearAutor(request):
#    if request.method == 'POST':
#        print(request.POST) # la salida es: <QueryDict: {'csrfmiddlewaretoken': ['#####'], 'nombre': ['1'], 'apellidos': ['2'], 'nacionalidad': ['3'], 'descripcion': ['4']}>
#        nom = request.POST.get('nombre')
#        ape = request.POST.get('apellidos')
#        nacio = request.POST.get('nacionalidad')
#        desc = request.POST.get('descripcion')
#        print(nom,ape,nacio,desc)
#        autor = Autor(nombre=nom, apellidos=ape, nacionalidad=nacio, descripcion=desc)
#        autor.save()
#        return redirect('libro:listar_autor')
#    return render(request, 'libro/crear_autor.html')
#
# Vistas basadas en funciones


def listarAutor(request):
    autores = Autor.objects.filter(estado=True)
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

#Eliminación Directa sin template
#def eliminarAutor(request, id):
#    autor = Autor.objects.get(id = id)
#    autor.delete()
#    return redirect('libro:listar_autor')


#Eliminación Directa por POST
#def eliminarAutor(request, id):
#    autor = Autor.objects.get(id = id)
#    if request.method == 'POST':
#        autor.delete()
#        return redirect('libro:listar_autor')
#    return render(request,'libro/eliminar_autor.html',{'autor':autor})

#Eliminación Logica: oculta de la vista del cliente con un estado (añadimos en el modelo de autor estado)
def eliminarAutor(request, id):
    autor = Autor.objects.get(id = id)
    if request.method == 'POST':
        autor.estado = False
        autor.save()
        return redirect('libro:listar_autor')
    return render(request,'libro/eliminar_autor.html',{'autor':autor})

