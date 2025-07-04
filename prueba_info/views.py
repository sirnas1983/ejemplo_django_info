from django.shortcuts import render

def prueba(request):
    contexto = {
        'mensaje' : '¡Hola Mundo!',
        'lista' : [1,'elemento dos',3,5]
    }
    return render(request, 'prueba.html', contexto)