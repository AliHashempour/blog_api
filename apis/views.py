from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics

from apis.serializers import ArticleSerializer, UserSerializer
from articles.models import Article


class ArticleListView(generics.ListCreateAPIView):
    queryset = Article.objects.filter(show=True)
    serializer_class = ArticleSerializer


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.filter(show=True)
    serializer_class = ArticleSerializer


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
