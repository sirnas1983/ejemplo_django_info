from django.urls import path

from app.articulo.views import ArticuloVistaBorrar, ArticuloVistaCrear, ArticuloVistaDetalle, ArticuloVistaEditar, ArticuloVistaVerTodos
from app.usuario.views import RegistrarUsuario

app_name = 'usuario' # importante para hacer navegacion con nombre de vistas

urlpatterns = [
    path('registro/', RegistrarUsuario.as_view() , name='registro')
    ]