from django.contrib import admin
from .models import Escola, Idioma, Professor, Estudante, Curso, Inscricao

admin.site.register(Escola)
admin.site.register(Idioma)
admin.site.register(Professor)
admin.site.register(Estudante)
admin.site.register(Curso)
admin.site.register(Inscricao)
