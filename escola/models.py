from django.db import models


class Escola(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Idioma(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome


class Estudante(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome


class Curso(models.Model):
    nome = models.CharField(max_length=100)
    escola = models.ForeignKey(
        Escola,
        on_delete=models.CASCADE,
        related_name="cursos"
    )
    idioma = models.ForeignKey(
        Idioma,
        on_delete=models.CASCADE,
        related_name="cursos"
    )
    professor = models.ForeignKey(
        Professor,
        on_delete=models.CASCADE,
        related_name="cursos"
    )
    estudantes = models.ManyToManyField(
        Estudante,
        through="Inscricao",
        related_name="cursos"
    )

    def __str__(self):
        return self.nome


class Inscricao(models.Model):
    estudante = models.ForeignKey(
        Estudante,
        on_delete=models.CASCADE,
        related_name="inscricoes"
    )
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name="inscricoes"
    )
    data_inscricao = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.estudante.nome} - {self.curso.nome}"

    class Meta:
        unique_together = ("estudante", "curso")
