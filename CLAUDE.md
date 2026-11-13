# CLAUDE.md — flix_api

Guia para o Claude Code trabalhar neste repositório. Leia antes de editar.

## O que é
API REST de **catálogo de filmes** — Django 4.2 + Django REST Framework + SimpleJWT (SQLite). Projeto pessoal de estudo/portfólio de José Roberto (JRFilho1503).

## Apps e domínio
- `genres`, `actors`, `movies` (FK para genre + M2M de actors), `reviews`, `authentication` (JWT).
- Endpoints sob **`/api/v1/`** — todos exigem token JWT, exceto a emissão (`/authentication/token/`).

## Stack
Python · Django 4.2 · DRF 3.14 · djangorestframework-simplejwt · flake8 · SQLite.

## Como rodar
```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Convenções
- **Lint:** flake8 (config em `.flake8`) — rode `flake8` antes de commitar.
- Cada app segue o padrão Django: `models.py`, `serializers.py`, `views.py`, `urls.py`, `migrations/`.
- Mantenha os endpoints sob `/api/v1/` e a **proteção JWT + permissões por rota**.

## Ao adicionar/alterar
- Novo recurso = model + serializer + view + url + migration; rode as migrations.
- Teste os endpoints com token JWT (ver exemplos no README).
- Se houver suíte de testes (DRF `APITestCase` / pytest-django), rode-a antes de commitar.

## Não faça
- Não commitar `db.sqlite3`, `SECRET_KEY` ou segredos (ver `.gitignore`).
- Não quebrar o contrato dos endpoints existentes sem atualizar o README.
