from django.urls import path, include
from apis.views import ArticleListView, ArticleDetailView

urlpatterns = [
    path('', ArticleListView.as_view(), name='api_article_list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='api_article_detail'),
]
