from django.db import models

# Create your models here.

class Pessoa(models.Model):
    name = models.TextField(max_length=255)
    password = models.CharField(max_length=255)
