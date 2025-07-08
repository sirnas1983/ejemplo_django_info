### 🧩 Tags comunes en templates de Django

| Tag                    | Uso                                              | Ejemplo                                                                 |
|------------------------|--------------------------------------------------|-------------------------------------------------------------------------|
| `{% if %}`             | Condicional                                      | `{% if user.is_authenticated %} Hola {% endif %}`                      |
| `{% if ... else %}`    | Condicional con alternativa                      | `{% if lista %} Ok {% else %} Vacío {% endif %}`                        |
| `{% for %}`            | Bucle sobre lista o queryset                     | `{% for obj in objetos %} {{ obj }} {% endfor %}`                       |
| `{% empty %}`          | Dentro de un `for`, para caso sin resultados     | `{% for x in lista %}...{% empty %} Nada para mostrar {% endfor %}`     |
| `{% block %}`          | Define un bloque para herencia de plantilla      | `{% block contenido %}...{% endblock %}`                                |
| `{% extends %}`        | Hereda de una plantilla base                     | `{% extends "miapp/base.html" %}`                                       |
| `{% include %}`        | Inserta otro template dentro del actual          | `{% include "partials/menu.html" %}`                                    |
| `{% load static %}`    | Habilita uso de archivos estáticos (CSS/JS/img)  | `{% load static %} <img src="{% static 'img/logo.png' %}">`             |
| `{% url %}`            | Genera URLs dinámicamente                        | `{% url 'miapp:detalle' articulo.id %}`                                 |
| `{% csrf_token %}`     | Previene ataques CSRF (obligatorio en formularios POST) | `<form>{% csrf_token %}</form>`                                  |
| `{# comentario #}`     | Comentario interno que no se muestra             | `{# Esto no aparece en el HTML #}`                                     |
