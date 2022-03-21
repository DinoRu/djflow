from django.contrib import admin
from .models import Category, Article, Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_on']


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
