from django.contrib import admin

from articles.models import Article


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = ['title', 'author', 'show', 'updated_at']


admin.site.register(Article, ArticleAdmin)
