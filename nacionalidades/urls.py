from django.urls import path
from . import views

urlpatterns = [

    path("", views.lista_nacionalidades, name="lista_nacionalidades"),
]
