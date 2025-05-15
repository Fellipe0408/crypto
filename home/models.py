from django.db import models
from django.contrib.auth.models import User
class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    data_postagem = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.usuario.username}: {self.texto}'