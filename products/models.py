from django.db import models


# Category model: Stores product categories.
# One category can have multiple products (One-to-Many relationship).
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    # Returns the category name when displaying the object.
    def __str__(self):
        return self.name


# Tag model: Stores tags that can be assigned to products.
# A tag can be associated with multiple products.
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    # Returns the tag name when displaying the object.
    def __str__(self):
        return self.name


# Product model: Stores the main product information.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # ForeignKey creates a Many-to-One relationship:
    # Each product belongs to one category,
    # but a category can contain multiple products.
    # PROTECT prevents deleting a category if products are linked to it.
    # related_name="products" allows accessing products using category.products.all().
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="products"
    )

    # Many-to-Many relationship:
    # A product can have multiple tags,
    # and each tag can belong to multiple products.
    # blank=True allows a product to exist without tags.
    tags = models.ManyToManyField(
        Tag,
        related_name="products",
        blank=True
    )

    # Automatically stores the date and time when a product is created.
    # This value is set only when the record is first created.
    created_at = models.DateTimeField(auto_now_add=True)

    # Returns the product name when displaying the object.
    def __str__(self):
        return self.name