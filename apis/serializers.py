from django.contrib.auth import get_user_model
from rest_framework import serializers

from articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ('id', 'created_at',)

    def validate(self, data):
        banned_words = ['LGBTQ', 'gay', 'pride']
        body = data['body']
        for word in banned_words:
            if word in body:
                raise serializers.ValidationError(
                    "we dont support gay rights here :)"
                )
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        exclude = ('password',)
