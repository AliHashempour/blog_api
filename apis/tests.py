from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from articles.models import Article


class ArticleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="tester",
            email="test@email.com",
            password="secret",
        )
        cls.article = Article.objects.create(
            author=cls.user,
            title="A good title",
            body="Nice body content",
        )

    def test_article_model(self):
        self.assertEqual(self.article.author.username, 'tester')
        self.assertEqual(self.article.title, 'A good title')
        self.assertEqual(self.article.body, 'Nice body content')
        self.assertEqual(str(self.article), 'A good title')

    def test_api_list_view(self):
        response = self.client.get(reverse('api_article_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Article.objects.count(), 1)

    def test_api_detail_view(self):
        response = self.client.get(
            reverse('api_article_detail', kwargs={'pk': self.article.id}),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'A good title')
        self.assertEqual(response.data['body'], 'Nice body content')
