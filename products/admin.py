
# Import Django's built-in admin functionality
from django.contrib import admin

# Import the database models that we want to manage through Django Admin
from .models import Category, Tag, Product


# =========================================
# 1. CATEGORY ADMIN CONFIGURATION
# =========================================

# Registers the Category model in the Django Admin interface
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    # Defines which columns are displayed in the category list
    list_display = ("name", "description")

    # Adds a search box to search categories by name
    search_fields = ("name",)


# =========================================
# 2. TAG ADMIN CONFIGURATION
# =========================================

# Registers the Tag model in the Django Admin interface
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):

    # Displays the tag name in the admin list
    list_display = ("name",)

    # Allows administrators to search tags by name
    search_fields = ("name",)


# =========================================
# 3. PRODUCT ADMIN CONFIGURATION
# =========================================

# Registers the Product model in the Django Admin interface
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    # Defines the columns displayed in the product list
    list_display = ("name", "category", "price", "created_at")

    # Adds sidebar filters for category, tags and creation date
    list_filter = ("category", "tags", "created_at")

    # Allows administrators to search products by name or description
    search_fields = ("name", "description")

    # Displays the Many-to-Many tags field using a horizontal selection interface
    # instead of the default multiple-selection box
    filter_horizontal = ("tags",)
