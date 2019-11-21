from django.db import models

# Create your models here.
class Autor(models.Model):
    id = models.AutoField(primary_key= True)
    #blank False = No permitira que sea guardado en blanco, null False = no recibe campos vacios
    nombre = models.CharField(max_length=50,blank=False,null=False)
    apellidos = models.CharField(max_length=200, blank=False,null=False)
    nacionalidad = models.CharField(max_length=50,blank=False,null=False)
    descripcion = models.TextField(blank=False,null=False)