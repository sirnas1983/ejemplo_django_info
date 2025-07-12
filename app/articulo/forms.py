from django import forms
from app.articulo.models import Articulo


class ArticuloFormulario(forms.ModelForm):

    class Meta:
        model = Articulo
        fields = ['titulo', 'subtitulo', 'contenido', 'categoria', 'esta_habilitado']
        widgets = {
            'titulo' : forms.TextInput(attrs={'class':'form-control'}),
            'subtitulo' : forms.TextInput(attrs={'class':'form-control'}),
            'contenido' : forms.TextInput(attrs={'class':'form-control'}),
            'categoria' : forms.Select(attrs={'class':'form-select'}),
            'esta_habilitado' : forms.CheckboxInput()
        }
     