# 🎬 flix_api — API de Catálogo de Filmes

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django%204.2-092E20?logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/Django%20REST-A30000?logo=django&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?logo=jsonwebtokens&logoColor=white)

**API REST** de um catálogo de filmes feita com **Django REST Framework**: gêneros, atores, filmes e avaliações, com **autenticação JWT** e **permissões por rota**.

## ✨ O que a API faz

- **CRUD** de **gêneros**, **atores**, **filmes** e **reviews**.
- **Filmes** relacionam **gênero** (FK) e **atores** (M2M), com data de lançamento e sinopse.
- **Reviews** com nota/stars por filme.
- **Autenticação JWT** (`djangorestframework-simplejwt`) e **permissões** customizadas por endpoint.

## 🧱 Apps

| App | Recurso |
| --- | --- |
| `genres` | Gêneros |
| `actors` | Atores |
| `movies` | Filmes (gênero, atores, lançamento, sinopse) |
| `reviews` | Avaliações dos filmes |
| `authentication` | Emissão/refresh de token JWT |

## 🔌 Endpoints

Todos sob o prefixo **`/api/v1/`** (exigem token JWT, exceto a emissão):

| Método | Rota | Descrição |
| --- | --- | --- |
| `POST` | `/authentication/token/` | Obter token (access + refresh) |
| `POST` | `/authentication/token/refresh/` | Renovar o access token |
| `GET/POST` | `/genres/` | Listar / criar gêneros |
| `GET/POST` | `/actors/` | Listar / criar atores |
| `GET/POST` | `/movies/` | Listar / criar filmes |
| `GET/POST` | `/reviews/` | Listar / criar avaliações |

## 🛠️ Stack

`Python` · `Django 4.2` · `Django REST Framework` · `SimpleJWT` · `SQLite`

## 🚀 Como rodar

```bash
git clone https://github.com/JRFilho1503/flix_api.git
cd flix_api

python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## 🔑 Exemplo de uso

```bash
# obter token
curl -X POST http://localhost:8000/api/v1/authentication/token/ \
  -d "username=SEU_USER&password=SUA_SENHA"

# listar filmes com o token
curl http://localhost:8000/api/v1/movies/ \
  -H "Authorization: Bearer <access_token>"
```

---

Projeto de estudo/prática em Django REST Framework. Sugestões são bem-vindas.
