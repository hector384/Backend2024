from django.db import models
from django.contrib.auth.models import User


class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    lugar = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Asistencia(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    confirmado = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.usuario.username} - {self.evento.nombre}'
