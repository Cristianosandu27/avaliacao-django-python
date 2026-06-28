from django.contrib import admin
from .models import Restaurante, Cliente, Reserva, Prato

admin.site.register(Restaurante)
admin.site.register(Cliente)
admin.site.register(Reserva)
admin.site.register(Prato)
