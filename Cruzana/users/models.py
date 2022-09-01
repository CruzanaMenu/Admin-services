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