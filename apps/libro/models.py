from django.db import models

# Create your models here.
class Autor(models.Model):
    id = models.AutoField(primary_key= True)
    #blank False = No permitira que sea guardado en blanco, null False = no recibe campos vacios
    nombre = models.CharField('Nombres',max_length=50,blank=False,null=False)
    apellidos = models.CharField('Apellidos',max_length=200, blank=False,null=False)
    nacionalidad = models.CharField('Nacionalidad',max_length=50,blank=False,null=False)
    descripcion = models.TextField('Descripción',blank=False,null=False)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = True,auto_now_add=False)

    #usamos los metadatos
    class Meta:
        #Definimos como queremos que se visualice en el panel administrativo
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre'] #atributo por el cualquiero ordenar
    
    #Cada vez que el objeto se liste nos muestre el campo nombre
    def __str__(self):
        return self.nombre

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo',blank=False,null=False, max_length=50)
    fecha_publicacion = models.DateField('Fecha de publicación', blank=False, null=False, auto_now=False, auto_now_add=False)
    #cada vez que se cree se actualizara el campo
    fecha_creacion = models.DateField('Fecha de creación', auto_now = True,auto_now_add=False)
    
    #Relación uno a uno: un autor solo podra tiene un libro o sino pondra error
    #autor_id = models.OneToOneField(Autor,on_delete = models.CASCADE)

    #Relación uno a muchos: un autor podra tener varios libros pero se crearan en diferente registros
    #autor_id = models.ForeignKey(Autor,on_delete = models.CASCADE)

    #Relacion muchos a mucho: un libro puede estar escrito por muchos autores y un autor pueden escribir varios libros
    autor_id = models.ManyToManyField(Autor)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']
    
    def __str__(self):
        return self.titulo