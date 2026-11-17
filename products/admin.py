
from django.contrib import admin
from .models import Category, Tag, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "created_at")
    list_filter = ("category", "tags", "created_at")
    search_fields = ("name", "description")
    filter_horizontal = ("tags",)
