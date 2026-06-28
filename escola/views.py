from django.shortcuts import render
from .models import Idioma, Curso


def cursos_por_idioma(request):
    idiomas = Idioma.objects.all()
    return render(request, "escola/cursos_por_idioma.html", {
        "idiomas": idiomas
    })


def estudantes_por_curso(request):
    cursos = Curso.objects.all()
    return render(request, "escola/estudantes_por_curso.html", {
        "cursos": cursos
    })
