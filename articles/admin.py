from django.contrib import admin
from .models import Article, Comment


class CommentInline(admin.TabularInline): 
    model = Comment
    extra = 0 # number of empty comments displayed, default is 3

class ArticleAdmin(admin.ModelAdmin): 
    inlines = [
        CommentInline,
    ]


admin.site.register(Article, ArticleAdmin) 
admin.site.register(Comment)
