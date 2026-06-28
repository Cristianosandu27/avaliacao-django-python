# Projeto Django — Avaliação Prática

Este projeto contém 3 aplicações Django:

- `biblioteca`
- `escola`
- `restaurante`

## Como correr o projeto

Abrir o terminal dentro da pasta do projeto e executar:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py seed_data
python manage.py runserver
```

Depois abrir no browser:

```text
http://127.0.0.1:8000/
```

## Páginas principais

Biblioteca:

```text
http://127.0.0.1:8000/biblioteca/generos/
http://127.0.0.1:8000/biblioteca/autores/
```

Escola:

```text
http://127.0.0.1:8000/escola/cursos-por-idioma/
http://127.0.0.1:8000/escola/estudantes-por-curso/
```

Restaurante:

```text
http://127.0.0.1:8000/restaurante/reservas-por-restaurante/
http://127.0.0.1:8000/restaurante/menu-por-restaurante/
```

## GitHub

Para enviar para GitHub:

```bash
git init
git add .
git commit -m "Projeto Django avaliação prática"
git branch -M main
git remote add origin URL_DO_REPOSITORIO
git push -u origin main
```
