from django.urls import path

from app.articulo.views import ArticuloVistaCrear, ArticuloVistaDetalle, ArticuloVistaEditar, ArticuloVistaVerTodos

app_name = 'articulo'

urlpatterns = [
    path('crear/', ArticuloVistaCrear.as_view() , name='crear'),
    path('', ArticuloVistaVerTodos.as_view() , name='lista'),
    path('detalle/<int:pk>',ArticuloVistaDetalle.as_view(), name='detalle'),
    path('editar/<int:pk>', ArticuloVistaEditar.as_view(), name='editar'),
    path('borrar/<int:pk>', ArticuloVistaCrear.as_view(), name='borrar')
]