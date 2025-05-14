from django.db import models

# Create your models here.

class Registros(models.Model):
    username = models.CharField(max_length=150)
    senha = models.CharField(max_length=128)

    def __str__(self):
        return self.username