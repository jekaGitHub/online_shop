from django.contrib import admin
from catalog.models import Product, Category, Article, Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    list_filter = ("category",)
    search_fields = ("name", "description")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "is_published", "views_count")
    list_filter = ("is_published",)
    search_fields = ("title", "description")


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ("id", "number_version", "name_version", "is_active_version", "product")
    list_filter = ("is_active_version", "product")
    search_fields = ("number_version",)
