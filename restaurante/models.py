from django.db import models


class Restaurante(models.Model):
    nome = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=150)
    capacidade = models.IntegerField()

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Reserva(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="reservas"
    )
    restaurante = models.ForeignKey(
        Restaurante,
        on_delete=models.CASCADE,
        related_name="reservas"
    )
    data = models.DateField()
    hora = models.TimeField()
    numero_pessoas = models.IntegerField()

    def __str__(self):
        return f"{self.cliente.nome} - {self.restaurante.nome} - {self.data}"


class Prato(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    restaurante = models.ForeignKey(
        Restaurante,
        on_delete=models.CASCADE,
        related_name="pratos"
    )

    def __str__(self):
        return self.nome
