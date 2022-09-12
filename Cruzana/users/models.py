from pickle import FALSE
from unittest.util import _MAX_LENGTH
from django.db import models

class Customer(models.Model):
    class Gender(models.TextChoices):
        male = "Masculino"
        female = "Femenino" 

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    telephone_number = models.DecimalField(max_digits=10, decimal_places=0)
    gender = models.CharField(
        max_length=10, 
        choices = Gender.choices,
        default=Gender.male)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.first_name

class Comida(models.Model):

    name_food = models.CharField(max_lenght=30)
    desc_small = models.CharField(max_length=70)
    desc_large = models.CharField(max_length=120)
    desc_full = models.CharField(max_length=200)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name_food

class Bebidas(models.Model):
    
    name_bebida = models.CharField(max_length=30)
    desc_bebida = models.CharField(max_length=50, null=FALSE)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name_bebida

class Pedidos(models.Model):

    date_pedido = models.DateField("date published")
    


    