from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cursos/', views.cursos, name='cursos'),
    path('profesores/', views.profesores, name='profesores'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('crear_entregable/', views.crear_entregable, name='crear_entregable'),
    path('crear_curso/', views.crear_curso, name='crear_curso'),
]
