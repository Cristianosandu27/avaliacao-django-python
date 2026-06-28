from django.shortcuts import render, get_object_or_404
from .models import Autor, Genero


def livros_por_genero(request):
    generos = Genero.objects.all()
    return render(request, "biblioteca/livros_por_genero.html", {
        "generos": generos
    })


def livros_por_autor(request):
    autores = Autor.objects.all()
    return render(request, "biblioteca/livros_por_autor.html", {
        "autores": autores
    })


def detalhe_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    return render(request, "biblioteca/detalhe_autor.html", {
        "autor": autor
    })
