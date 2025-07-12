from django.apps import AppConfig


class ArticuloConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.articulo' # Atenti: Aca hay que agregar como prefijo el nombre de la carpeta donde esta alojada la app
