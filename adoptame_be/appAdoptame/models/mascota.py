from django.db import models
from django.contrib.postgres.fields import ArrayField

class Mascota(models.Model):
    id = models.AutoField(primary_key=True)
    especie = models.CharField(max_length=64, choices=(
        ('G', 'Gato'),
        ('P', 'Perro'),
    ))
    edad = models.PositiveIntegerField(default=0, null=False)
    nombre = models.CharField(max_length=100, null=False)
    tamaño = models.CharField(max_length=64, choices=(
        ('P', 'Pequeño'),
        ('M', 'Mediano'),
        ('G', 'Grande'),
    ))
    descripcion = models.TextField(null=True, blank=False)
    sexo = models.CharField(max_length=64, choices=(
        ('M', 'Macho'),
        ('H', 'Hembra'),
    ))
    personalidad = models.CharField(max_length=100, null=True, blank=True)
    personalidades = ArrayField(models.CharField(max_length=100, blank=True, null=True),default=list, size=3, null=True, blank=True)
    esterilizado = models.BooleanField(default=False)
    desparasitado = models.BooleanField(default=False )
    salud = models.CharField(max_length=100, null=True, blank=True)
    imagen = models.ImageField(upload_to="img/", null=True, blank=True)
    adoptado = models.BooleanField(default=False, null=True, blank=True)
