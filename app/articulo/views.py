from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from app.articulo.forms import ArticuloFormulario
from django.contrib.auth.mixins import UserPassesTestMixin
from app.articulo.models import Articulo

class ArticuloVistaVerTodos(ListView):
    model = Articulo
    context_object_name = 'articulos'
    template_name = 'articulo/ver-todos.html'

class ArticuloVistaCrear(UserPassesTestMixin, CreateView):

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.rol == 'escritor'

    model = Articulo
    form_class = ArticuloFormulario
    template_name = 'articulo/crear.html'
    success_url = reverse_lazy('articulo:lista')

    def form_valid(self, form): # Esto es para agregar el usuario automaticamente a la hora de crear el articulo
        form.instance.creado_por = self.request.user
        return super().form_valid(form)

class ArticuloVistaDetalle(DetailView):
    model= Articulo
    template_name = "articulo/detalle.html"
    context_object_name = 'articulo'

class ArticuloVistaEditar(UserPassesTestMixin,UpdateView):

    def test_func(self):
        return self.request.user == self.get_object().creado_por or self.request.user.is_superuser

    model = Articulo
    form_class = ArticuloFormulario
    context_object_name = 'articulo'
    template_name = 'articulo/crear.html'
    success_url = reverse_lazy('articulo:lista')

class ArticuloVistaBorrar(UserPassesTestMixin, DeleteView):

    def test_func(self):
        return self.request.user == self.get_object().creado_por or self.request.user.is_superuser

    model = Articulo
    template_name = 'articulo/confirmar-borrado.html'
    success_url = reverse_lazy('articulo:lista')