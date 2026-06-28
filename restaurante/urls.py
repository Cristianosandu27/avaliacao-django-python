from django.urls import path
from . import views

urlpatterns = [
    path("reservas-por-restaurante/", views.reservas_por_restaurante, name="reservas_por_restaurante"),
    path("menu-por-restaurante/", views.menu_por_restaurante, name="menu_por_restaurante"),
]
