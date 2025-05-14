from django.contrib.auth.models import AbstractUser , Group, Permission
from django.db import models

class CustomUser (AbstractUser ):
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Adicione um related_name único
        blank=True,
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Adicione um related_name único
        blank=True,
    )