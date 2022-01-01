from django.db import models
from django.core.validators import RegexValidator
from django.db.models.fields import AutoField
from django.db.models.fields.related import ForeignKey


class Adoptante(models.Model):
    cedulaAdoptante = models.IntegerField(primary_key=True, default=0)
    #Validador de celular
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    nombre = models.CharField(max_length=30, null=False, blank=False)
    apellido = models.CharField(max_length=60, null=False,blank=False)
    email = models.EmailField(null=False,blank=False)
    edad = models.IntegerField(default=18, null=False,blank=False)
    telefono = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    ciudad = models.CharField(max_length=20,blank=False)
    direccion = models.CharField(max_length=60,blank=False)
