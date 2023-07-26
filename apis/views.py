from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from apis.serializers import ArticleSerializer, UserSerializer
from articles.models import Article
from apis.permissions import IsAuthorOrAdminElseReadOnly


class ArticleListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Article.objects.filter(show=True)
    serializer_class = ArticleSerializer


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrAdminElseReadOnly,)
    queryset = Article.objects.filter(show=True)
    serializer_class = ArticleSerializer


class UserListView(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
