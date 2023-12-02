from django.contrib import admin
from .models import Curso, Profesor, Entregable, Estudiante

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "camada")
    list_filter =  ("nombre", "camada")
    search_fields = ("nombre", "camada")
    
@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "email", "profesion")
    list_filter =  ("nombre", "apellido", "email", "profesion")
    search_fields = ("nombre", "apellido", "email", "profesion")
