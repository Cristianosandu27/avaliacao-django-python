from django.contrib import admin
from .models import Autor, Genero, Livro

admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(Livro)
