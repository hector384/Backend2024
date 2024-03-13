from django.db import models


class School(models.Model):
    name = models.TextField(max_length=100)
    created = models.DateTimeField()
    address = models.TextField(max_length=100)
    id_user = models.CharField()
    description = models.TextField()
    city = models.TextField(max_length=50)
    mision = models.TextField(max_length=500)
    vision = models.TextField(max_length=500)
    policy = models.TextField(max_length=500)
    id_image = models.TextField(max_length=100)
    route = models.TextField(max_length=100)
    sizes = models.TextField(max_length=100)
    banner = models.TextField(max_length=100)
    password = models.TextField(max_length=20)
    email = models.EmailField(max_length=100)
    telephone = models.TextField(max_length=100)
    is_instructor = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
