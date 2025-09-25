from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Alimento(models.Model):
    nombre = models.CharField(max_length=100)
    calorias = models.FloatField()
    proteinas = models.FloatField()
    carbohidratos = models.FloatField()
    grasas = models.FloatField()

    def __str__(self):
        return self.nombre

class RegistroComida(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE)
    cantidad = models.FloatField()

    def __str__(self):
        return f"{self.usuario.alimento} - {self.alimento.nombre} ({self.fecha})"