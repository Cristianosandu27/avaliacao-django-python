from django.urls import path
from . import views

urlpatterns = [
    path("generos/", views.livros_por_genero, name="livros_por_genero"),
    path("autores/", views.livros_por_autor, name="livros_por_autor"),
    path("autor/<int:autor_id>/", views.detalhe_autor, name="detalhe_autor"),
]
