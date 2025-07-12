from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class Usuario(AbstractBaseUser):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    roles = []
    
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['nombre', 'apellido']