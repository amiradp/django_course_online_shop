from django.contrib import admin

from .models import Product, Comment, Category


class CommentInLine(admin.TabularInline):
    model = Comment
    fields = ['author', 'body', 'stars', 'active', ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active', 'category', ]

    inlines = [
        CommentInLine,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'body', 'stars', 'active', ]


admin.site.register(Category)
