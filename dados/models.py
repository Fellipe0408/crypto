from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.TextField(max_length=255)
    email = models.EmailField(max_length=255)
