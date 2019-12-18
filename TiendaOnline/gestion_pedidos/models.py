from django.db import models

# Create your models here.

# crear los modelos


class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=7)


class Articulo(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=50)
    precio = models.IntegerField()


class Pedido(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entrada = models.BooleanField()
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)


class Estado(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entrada = models.BooleanField()
    salida = models.BooleanField()

class Detalle(models.Model):
    cliente = models.ManyToManyField(Cliente)
    Pedido = models.ManyToManyField(Articulo)