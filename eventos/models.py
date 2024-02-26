from django.db import models
from django.contrib.auth.models import User
from escuelas.models import School


class Evento(models.Model):
    id_school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.TextField(max_length=100)
    date_evenet = models.DateTimeField()
    place = models.TextField(max_length=100)
    description = models.TextField()
    id_picture = models.TextField(max_length=100)
    route = models.TextField(max_length=100)
    sizes = models.TextField(max_length=100)

    def __str__(self):
        return self.nombre


class Asistencia(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    confirmado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.usuario.username} - {self.evento.nombre}"
