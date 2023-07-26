from django.urls import path, include
from apis.views import ArticleListView

urlpatterns = [
    path('', ArticleListView.as_view(), name='api_article_list'),
]
