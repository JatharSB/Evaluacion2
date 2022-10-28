from email.policy import default
from django.db import models
from django.forms import CharField

# Create your models here.
reserva_estado = [
    ('Reservado','Reservado'),
    ('Completado','Completado'),
    ('Anulada','Anulada'),
    ('No Asisten','No Asisten'),
]

class reserva(models.Model):
    id = models.IntegerField 
    nombre = models.CharField(max_length=20)
    fono = models.CharField(max_length=9)
    fechareserva = models.DateField()
    hora = models.TimeField()
    cantidad = models.IntegerField()
    estado = models.CharField(
        max_length = 20,
        null=False, blank=False,
        choices=reserva_estado,
        default=1)
    observacion = models.CharField(max_length=40)