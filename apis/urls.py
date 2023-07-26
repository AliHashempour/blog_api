from django.urls import path, include
from apis.views import ArticleListView, ArticleDetailView, UserListView, UserDetailView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('token-auth/', obtain_auth_token),
    path('articles', ArticleListView.as_view(), name='api_article_list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='api_article_detail'),
    path('users', UserListView.as_view(), name='api_user_list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='api_user_detail'),
]
