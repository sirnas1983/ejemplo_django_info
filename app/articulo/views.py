from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from app.articulo.forms import ArticuloFormulario
from app.articulo.models import Articulo

class ArticuloVistaCrear(CreateView):
    model = Articulo
    form_class = ArticuloFormulario
    template_name = 'articulo/crear.html'
    success_url = reverse_lazy('articulo:lista')

class ArticuloVistaVerTodos(ListView):
    model = Articulo
    context_object_name = 'articulos'
    template_name = 'articulo/ver-todos.html'

class ArticuloVistaDetalle(DetailView):
    model= Articulo
    template_name = "articulo/detalle.html"
    context_object_name = 'articulo'

class ArticuloVistaEditar(UpdateView):
    model = Articulo
    form_class = ArticuloFormulario
    template_name = 'articulo/crear.html'
    success_url = reverse_lazy('articulo:lista')

class ArticuloVistaEditar(DeleteView):
    model = Articulo
