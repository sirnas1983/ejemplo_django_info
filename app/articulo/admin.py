from django.contrib import admin

from app.articulo.models import Articulo, Categoria

# Register your models here.
# Si no hacemos esto no vamos a poder administrar estas clases desde el ADMIN de Django
@admin.register(Categoria)
class CategoriaAdministrador(admin.ModelAdmin):
    list_display = ['id', 'nombre']

@admin.register(Articulo)
class ArticuloAdministrador(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'subtitulo', 'contenido', 'fecha_creacion']