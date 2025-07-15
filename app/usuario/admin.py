from django.contrib import admin

from app.usuario.models import Usuario

# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'email', 'is_staff', 'rol']