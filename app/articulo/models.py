from django.db import models

from app.usuario.models import Usuario

# Create your models here.
class Categoria(models.Model):

    nombre = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.nombre.upper()

class Articulo(models.Model):

    titulo = models.CharField(max_length=80)
    subtitulo = models.CharField(max_length=140)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    esta_habilitado = models.BooleanField(default=True)
    imagen_principal = models.ImageField(upload_to='articulos/imagenes', null=True, blank=True) # Instalar desde PIP la libreria PILLOW
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    creado_por = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.titulo