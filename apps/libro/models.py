from django.db import models

# Create your models here.
class Autor(models.Model):
    id = models.AutoField(primary_key= True)
    #blank False = No permitira que sea guardado en blanco, null False = no recibe campos vacios
    nombre = models.CharField('Nombres',max_length=50,blank=False,null=False)
    apellidos = models.CharField('Apellidos',max_length=200, blank=False,null=False)
    nacionalidad = models.CharField('Nacionalidad',max_length=50,blank=False,null=False)
    descripcion = models.TextField('Descripción',blank=False,null=False)

    #usamos los metadatos
    class Meta:
        #Definimos como queremos que se visualice en el panel administrativo
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre'] #atributo por el cualquiero ordenar
    
    #Cada vez que el objeto se liste nos muestre el campo nombre
    def __str__(self):
        return self.nombre
    