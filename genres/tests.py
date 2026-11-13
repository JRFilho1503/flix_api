from django.contrib.auth.models import User, Permission
from rest_framework import status
from rest_framework.test import APITestCase

from genres.models import Genre


class GenreAPITestCase(APITestCase):
    """Cobre autenticação (401), permissão (403) e CRUD do recurso Genre."""

    def setUp(self):
        self.user = User.objects.create_user(username="qa", password="qa123456")
        perms = Permission.objects.filter(
            content_type__app_label="genres",
            codename__in=["view_genre", "add_genre", "change_genre", "delete_genre"],
        )
        self.user.user_permissions.set(perms)
        self.genre = Genre.objects.create(name="Ficção Científica")
        self.list_url = "/api/v1/genres/"
        self.detail_url = f"/api/v1/genres/{self.genre.id}/"

    def test_listar_sem_autenticacao_retorna_401(self):
        resp = self.client.get(self.list_url)
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_usuario_sem_permissao_retorna_403(self):
        sem_perm = User.objects.create_user(username="noperm", password="x1234567")
        self.client.force_authenticate(user=sem_perm)
        resp = self.client.get(self.list_url)
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)

    def test_listar_generos(self):
        self.client.force_authenticate(user=self.user)
        resp = self.client.get(self.list_url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data), 1)

    def test_criar_genero(self):
        self.client.force_authenticate(user=self.user)
        resp = self.client.post(self.list_url, {"name": "Comédia"})
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Genre.objects.count(), 2)

    def test_recuperar_genero(self):
        self.client.force_authenticate(user=self.user)
        resp = self.client.get(self.detail_url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data["name"], "Ficção Científica")

    def test_atualizar_genero(self):
        self.client.force_authenticate(user=self.user)
        resp = self.client.put(self.detail_url, {"name": "Drama"})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.genre.refresh_from_db()
        self.assertEqual(self.genre.name, "Drama")

    def test_remover_genero(self):
        self.client.force_authenticate(user=self.user)
        resp = self.client.delete(self.detail_url)
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Genre.objects.count(), 0)
