from django import forms
from app.usuario.models import Usuario
from django.contrib.auth.forms import UserCreationForm


class RegistroForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = ['email', 'nombre', 'apellido', 'rol', 'password1', 'password2']