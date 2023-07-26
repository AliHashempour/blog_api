from django.urls import path, include
from apis.views import ArticleListView, ArticleDetailView, UserListView, UserDetailView

urlpatterns = [
    path('articles', ArticleListView.as_view(), name='api_article_list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='api_article_detail'),
    path('users', UserListView.as_view(), name='api_user_list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='api_user_detail'),
]
