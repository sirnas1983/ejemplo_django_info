from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from django.contrib.auth import login

from app.usuario.forms import RegistroForm
from app.usuario.models import Usuario

# Create your views here.


class RegistrarUsuario(CreateView):
    model = Usuario
    form_class = RegistroForm
    template_name = 'usuario/registro.html'
    success_url = reverse_lazy('articulo:lista')

    def form_valid(self, form):
        respuesta = super().form_valid(form)
        login(self.request, self.object)
        return respuesta