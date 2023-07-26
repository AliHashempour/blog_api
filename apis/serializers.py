from django.contrib.auth.models import User
from rest_framework import serializers

from articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ('id', 'created_at',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)
