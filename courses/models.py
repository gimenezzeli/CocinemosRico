from django.db import models
#from django.contrib.auth.models import User

CONDITION_CHOICES1={
    ('Curso Chef', 'Curso Chef'),
    ('Curso Pasteleria', 'Curso Pasteleria'),
}

CONDITION_CHOICES2={
        ('dni','DNI'),
        ('cedula de identidad', 'Cédula de identidad'),
        ('pasaporte','Pasaporte'),
    }

class Course(models.Model):
    course=models.CharField(max_length=20, choices=CONDITION_CHOICES1, verbose_name='Curso a elegir')
    name = models.CharField(max_length=100, verbose_name='Nombre')
    last_name = models.CharField(max_length=100, verbose_name='Apellido')
    document= models.CharField(max_length=20, choices=CONDITION_CHOICES2,verbose_name='Tipo de documento')
    number_document= models.CharField(max_length=15,verbose_name='Numero de documento')
    birth_date= models.DateField(null=True, blank=True, verbose_name='Fecha de nacimiento')
    email= models.EmailField(verbose_name='Email')