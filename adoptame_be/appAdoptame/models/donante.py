from django.db import models
#importamos la clase del modelo de referencia de fk:

class Donante(models.Model):
    registro_donante = models.AutoField(primary_key=True)
    fecha = models.DateField(null=False)
    email = models.EmailField(null=False, blank=False,default="")
    nombre = models.CharField(max_length=40, null=False, blank=False)
    tipo_transaccion = models.CharField(max_length=50,null=True, blank=True,default="",choices=(
        ('A', 'Consignación'),
        ('B','Tarjeta débito'),
        ('C','KviPlata'),
        ('D', "Xequi"),
        ('E','Efectivo'),
        ('F','Otro')
    ))
    cantidad = models.FloatField(null=True, blank=True, default=0)
    comentarios = models.TextField(null=True, blank=True, default="")
