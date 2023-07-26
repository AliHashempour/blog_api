from django.shortcuts import render
from rest_framework import generics

from apis.serializers import ArticleSerializer
from articles.models import Article


class ArticleListView(generics.ListCreateAPIView):
    queryset = Article.objects.filter(show=True)
    serializer_class = ArticleSerializer
