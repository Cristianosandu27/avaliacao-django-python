from django.shortcuts import render
from .models import Restaurante


def reservas_por_restaurante(request):
    restaurantes = Restaurante.objects.all()
    return render(request, "restaurante/reservas_por_restaurante.html", {
        "restaurantes": restaurantes
    })


def menu_por_restaurante(request):
    restaurantes = Restaurante.objects.all()
    return render(request, "restaurante/menu_por_restaurante.html", {
        "restaurantes": restaurantes
    })
