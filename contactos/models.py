from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre=models.CharField(max_length=100)
    telefono=models.CharField(max_length=30)
    fechanacimiento=models.DateField()
    numerodepie=models.IntegerField()