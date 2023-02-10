from django.db import models

class Recipes(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    ingredients = models.CharField(max_length=250, verbose_name='Ingredientes')
    description = models.CharField(max_length=1000, verbose_name='Descripcion')
    image= models.ImageField(upload_to='recipes', null=True, blank=True, verbose_name='Imagen')

