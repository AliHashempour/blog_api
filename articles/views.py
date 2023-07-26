from django.shortcuts import render
from django.views.generic import ListView, DetailView

from articles.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

    def get_queryset(self):
        return Article.objects.filter(show=True)


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
