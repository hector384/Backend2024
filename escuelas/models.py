from django.db import models

class School(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField()
    address = models.CharField(max_length=100)
    description = models.TextField()
    city = models.CharField(max_length=50)
    mision = models.CharField(max_length=500)
    vision = models.CharField(max_length=500)
    policy = models.CharField(max_length=500)
    id_image = models.CharField(max_length=100)
    route = models.CharField(max_length=100)
    sizes = models.CharField(max_length=100)
    banner = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    telephone = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

