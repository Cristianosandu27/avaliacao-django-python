from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def home(request):
    return render(request, "home.html")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("biblioteca/", include("biblioteca.urls")),
    path("escola/", include("escola.urls")),
    path("restaurante/", include("restaurante.urls")),
    path("nacionalidades/", include("nacionalidades.urls")),
]
