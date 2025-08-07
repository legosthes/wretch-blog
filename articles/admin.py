from django.contrib import admin
from .models import Article

# Register your models here.

# 讓django的後台幫我們管理
class ArticleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Article,ArticleAdmin)