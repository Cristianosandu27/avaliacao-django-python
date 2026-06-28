from datetime import date, time
from django.core.management.base import BaseCommand

from biblioteca.models import Autor, Genero, Livro
from escola.models import Escola, Idioma, Professor, Estudante, Curso, Inscricao
from restaurante.models import Restaurante, Cliente, Reserva, Prato


class Command(BaseCommand):
    help = "Cria dados de exemplo para as 3 aplicações."

    def handle(self, *args, **options):
        self.criar_biblioteca()
        self.criar_escola()
        self.criar_restaurante()
        self.stdout.write(self.style.SUCCESS("Dados de exemplo criados com sucesso."))

    def criar_biblioteca(self):
        autor_a, _ = Autor.objects.get_or_create(nome="Autor A")
        autor_b, _ = Autor.objects.get_or_create(nome="Autor B")
        autor_c, _ = Autor.objects.get_or_create(nome="Autor C")

        romance, _ = Genero.objects.get_or_create(nome="Romance")
        aventura, _ = Genero.objects.get_or_create(nome="Aventura")
        poesia, _ = Genero.objects.get_or_create(nome="Poesia")

        livro1, _ = Livro.objects.get_or_create(titulo="Livro 1", autor=autor_a)
        livro1.generos.set([romance, aventura])

        livro2, _ = Livro.objects.get_or_create(titulo="Livro 2", autor=autor_b)
        livro2.generos.set([romance])

        livro3, _ = Livro.objects.get_or_create(titulo="Livro 3", autor=autor_b)
        livro3.generos.set([poesia])

        livro4, _ = Livro.objects.get_or_create(titulo="Livro 4", autor=autor_c)
        livro4.generos.set([aventura])

    def criar_escola(self):
        escola, _ = Escola.objects.get_or_create(nome="Escola Línguas+")

        ingles, _ = Idioma.objects.get_or_create(nome="Inglês")
        frances, _ = Idioma.objects.get_or_create(nome="Francês")
        espanhol, _ = Idioma.objects.get_or_create(nome="Espanhol")

        prof_joao, _ = Professor.objects.get_or_create(
            email="joao@escola.pt",
            defaults={"nome": "Professor João"}
        )
        prof_ana, _ = Professor.objects.get_or_create(
            email="ana@escola.pt",
            defaults={"nome": "Professora Ana"}
        )
        prof_carlos, _ = Professor.objects.get_or_create(
            email="carlos@escola.pt",
            defaults={"nome": "Professor Carlos"}
        )

        maria, _ = Estudante.objects.get_or_create(
            email="maria@email.pt",
            defaults={"nome": "Maria"}
        )
        pedro, _ = Estudante.objects.get_or_create(
            email="pedro@email.pt",
            defaults={"nome": "Pedro"}
        )
        ana, _ = Estudante.objects.get_or_create(
            email="ana@email.pt",
            defaults={"nome": "Ana"}
        )

        ingles_a1, _ = Curso.objects.get_or_create(
            nome="Inglês A1",
            escola=escola,
            idioma=ingles,
            professor=prof_joao
        )
        frances_a1, _ = Curso.objects.get_or_create(
            nome="Francês A1",
            escola=escola,
            idioma=frances,
            professor=prof_ana
        )
        espanhol_a1, _ = Curso.objects.get_or_create(
            nome="Espanhol A1",
            escola=escola,
            idioma=espanhol,
            professor=prof_carlos
        )

        Inscricao.objects.get_or_create(estudante=maria, curso=ingles_a1)
        Inscricao.objects.get_or_create(estudante=pedro, curso=ingles_a1)
        Inscricao.objects.get_or_create(estudante=ana, curso=ingles_a1)
        Inscricao.objects.get_or_create(estudante=maria, curso=frances_a1)
        Inscricao.objects.get_or_create(estudante=pedro, curso=espanhol_a1)

    def criar_restaurante(self):
        sabores, _ = Restaurante.objects.get_or_create(
            nome="Sabores do Sul",
            defaults={"localizacao": "Portimão", "capacidade": 80}
        )
        mar_azul, _ = Restaurante.objects.get_or_create(
            nome="Mar Azul",
            defaults={"localizacao": "Albufeira", "capacidade": 60}
        )

        maria, _ = Cliente.objects.get_or_create(
            email="maria.cliente@email.pt",
            defaults={"nome": "Maria Silva", "telefone": "910000001"}
        )
        pedro, _ = Cliente.objects.get_or_create(
            email="pedro.cliente@email.pt",
            defaults={"nome": "Pedro Costa", "telefone": "910000002"}
        )

        Reserva.objects.get_or_create(
            cliente=maria,
            restaurante=sabores,
            data=date(2026, 7, 10),
            hora=time(20, 0),
            numero_pessoas=4
        )
        Reserva.objects.get_or_create(
            cliente=pedro,
            restaurante=sabores,
            data=date(2026, 7, 11),
            hora=time(21, 0),
            numero_pessoas=2
        )
        Reserva.objects.get_or_create(
            cliente=maria,
            restaurante=mar_azul,
            data=date(2026, 7, 12),
            hora=time(19, 30),
            numero_pessoas=3
        )

        Prato.objects.get_or_create(nome="Bacalhau à Brás", restaurante=sabores, defaults={"preco": 12.50})
        Prato.objects.get_or_create(nome="Frango Grelhado", restaurante=sabores, defaults={"preco": 9.00})
        Prato.objects.get_or_create(nome="Arroz de Marisco", restaurante=sabores, defaults={"preco": 18.00})
        Prato.objects.get_or_create(nome="Sardinha Assada", restaurante=mar_azul, defaults={"preco": 10.00})
        Prato.objects.get_or_create(nome="Dourada Grelhada", restaurante=mar_azul, defaults={"preco": 14.00})
