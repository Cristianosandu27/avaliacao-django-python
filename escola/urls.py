from django.urls import path
from . import views

urlpatterns = [
    path("cursos-por-idioma/", views.cursos_por_idioma, name="cursos_por_idioma"),
    path("estudantes-por-curso/", views.estudantes_por_curso, name="estudantes_por_curso"),
]
