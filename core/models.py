from django.db import models
from django.contrib.auth.models import User

# Ejemplo de modelo para la configuración del sitio


class Sitio(models.Model):
    nombre = models.CharField(max_length=100)
    slogan = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='sitio/', blank=True, null=True)

    def __str__(self):
        return self.nombre

# Ejemplo de modelo para la configuración de usuarios


class ConfiguracionUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    sitio_web = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.usuario.username
