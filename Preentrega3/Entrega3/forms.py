from django import forms
from .models import Profesor, Curso, Entregable

class ProfesorFormulario(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'email', 'profesion']


class form_entregas(forms.ModelForm):
    class Meta:
        model = Entregable
        fields = ['nombre', 'fecha_entrega', 'entregado']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'camada']

    
