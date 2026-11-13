import datetime

from django.contrib.auth.models import User, Permission
from rest_framework import status
from rest_framework.test import APITestCase

from genres.models import Genre
from actors.models import Actor
from movies.models import Movie


class MovieAPITestCase(APITestCase):
    """Cobre CRUD com relações (FK gênero + M2M atores) e as validações de negócio."""

    def setUp(self):
        self.user = User.objects.create_user(username="qa", password="qa123456")
        perms = Permission.objects.filter(
            content_type__app_label="movies",
            codename__in=["view_movie", "add_movie", "change_movie", "delete_movie"],
        )
        self.user.user_permissions.set(perms)
        self.client.force_authenticate(user=self.user)
        self.genre = Genre.objects.create(name="Ação")
        self.actor = Actor.objects.create(name="Fulano de Tal")
        self.list_url = "/api/v1/movies/"

    def _payload(self, **over):
        p = {
            "title": "Filme X", "genre": self.genre.id,
            "release_date": "2020-01-01", "actors": [self.actor.id], "resume": "um resumo",
        }
        p.update(over)
        return p

    def test_criar_movie_com_genero_e_atores(self):
        resp = self.client.post(self.list_url, self._payload(), format="json")
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 1)
        self.assertEqual(Movie.objects.first().actors.count(), 1)

    def test_release_date_anterior_a_1900_e_invalida(self):
        resp = self.client.post(self.list_url, self._payload(release_date="1899-01-01"), format="json")
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("release_date", resp.data)

    def test_resume_acima_de_500_caracteres_e_invalido(self):
        resp = self.client.post(self.list_url, self._payload(resume="x" * 501), format="json")
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("resume", resp.data)

    def test_listar_movies(self):
        m = Movie.objects.create(title="M1", genre=self.genre, release_date=datetime.date(2020, 1, 1))
        m.actors.add(self.actor)
        resp = self.client.get(self.list_url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(resp.data), 1)
