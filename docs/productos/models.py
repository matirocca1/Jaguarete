from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

class Categorias(models.Model):
    nombre=models.CharField(max_length=15)
    descripcion=models.CharField(max_length=100)

    def __str__(self):
        return (self.nombre)

class Productos(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=20)
    imagen=models.ImageField(upload_to= 'productos')
    descripcion=models.CharField(max_length=100)
    precio=models.FloatField()
    categorias=models.ForeignKey(Categorias, on_delete=CASCADE)

    def __str__(self):
        return (self.nombre)
