from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from apis.serializers import ArticleSerializer, UserSerializer
from articles.models import Article
from apis.permissions import IsAuthorOrAdminElseReadOnly


class ArticleListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Article.objects.filter(show=True)
    serializer_class = ArticleSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['author__username', 'show']


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrAdminElseReadOnly,)
    queryset = Article.objects.filter(show=True)
    serializer_class = ArticleSerializer


class UserListView(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['username', 'email', 'is_staff', 'is_active']


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
