from django.contrib import admin
from django.urls import path, include

from articles.views import ArticleListView

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
]
