from django.shortcuts import render, redirect
from .forms import form_entregas, ProfesorFormulario, CursoForm
from .models import Estudiante, Curso, Profesor, Entregable

def index(request):
    return render(request, 'base.html')

def cursos(request):
    return render(request, 'cursos.html')

def profesores(request):
    return render(request, 'profesores.html')

def estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes.html', {'estudiantes': estudiantes})

def crear_entregable(request):
    if request.method == 'POST':
        form = form_entregas(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirige a la página de inicio después de guardar un nuevo entregable
    else:
        form = form_entregas()
    return render(request, 'form_entregas.html', {'form': form})
    
def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cursos')  # Redirige a la página de cursos después de guardar un nuevo curso
    else:
        form = CursoForm()
    return render(request, 'crear_curso.html', {'form': form})
