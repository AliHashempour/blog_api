from django.contrib import admin
from django.urls import path, include

from articles.views import ArticleListView, ArticleDetailView

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
]
