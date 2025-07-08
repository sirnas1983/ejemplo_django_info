from django.db import models

# Create your models here.
class Categoria(models.Model):

    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Articulo(models.Model):

    titulo = models.CharField(max_length=80)
    subtitulo = models.CharField(max_length=140)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    esta_habilitado = models.BooleanField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo