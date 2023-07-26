from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.title
