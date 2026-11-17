
from django.core.management.base import BaseCommand
from django.db import transaction

from products.models import Category, Tag, Product


class Command(BaseCommand):
    help = "Populate the database with electronics catalogue sample data"

    @transaction.atomic
    def handle(self, *args, **kwargs):

        # 1. Categories - exactly 5
        categories_data = [
            {
                "name": "Smartphones",
                "description": "Smartphones and mobile communication devices."
            },
            {
                "name": "Laptops",
                "description": "Personal and professional laptop computers."
            },
            {
                "name": "Tablets",
                "description": "Tablets and portable touchscreen devices."
            },
            {
                "name": "Audio",
                "description": "Headphones, earbuds and wireless speakers."
            },
            {
                "name": "Cameras",
                "description": "Digital cameras and professional photography equipment."
            },
        ]

        categories = {}

        for item in categories_data:
            category, _ = Category.objects.update_or_create(
                name=item["name"],
                defaults={"description": item["description"]}
            )
            categories[item["name"]] = category

        # 2. Tags - exactly 10
        tags_data = [
            "Apple",
            "Samsung",
            "Sony",
            "Dell",
            "Lenovo",
            "Google",
            "Wireless",
            "Bluetooth",
            "Premium",
            "Gaming",
        ]

        tags = {}

        for name in tags_data:
            tag, _ = Tag.objects.get_or_create(name=name)
            tags[name] = tag

        # 3. Products - exactly 20
        products_data = [
            {
                "name": "iPhone 17 Pro",
                "description": "Apple flagship smartphone with advanced camera system and A-series processor.",
                "price": "1599.00",
                "category": "Smartphones",
                "tags": ["Apple", "Premium"]
            },
            {
                "name": "iPhone 17",
                "description": "Apple smartphone designed for everyday performance and photography.",
                "price": "1129.00",
                "category": "Smartphones",
                "tags": ["Apple"]
            },
            {
                "name": "Samsung Galaxy S26 Ultra",
                "description": "Samsung flagship smartphone with a large display and advanced camera capabilities.",
                "price": "1899.00",
                "category": "Smartphones",
                "tags": ["Samsung", "Premium"]
            },
            {
                "name": "Samsung Galaxy S26",
                "description": "Premium Samsung smartphone with powerful performance and modern design.",
                "price": "1299.00",
                "category": "Smartphones",
                "tags": ["Samsung"]
            },
            {
                "name": "Google Pixel 10 Pro",
                "description": "Google smartphone featuring advanced computational photography and AI features.",
                "price": "1349.00",
                "category": "Smartphones",
                "tags": ["Google", "Premium"]
            },
            {
                "name": "MacBook Air 15-inch M4",
                "description": "Lightweight Apple laptop with M4 processor and high-resolution display.",
                "price": "1799.00",
                "category": "Laptops",
                "tags": ["Apple", "Premium"]
            },
            {
                "name": "MacBook Pro 14-inch",
                "description": "Professional Apple laptop designed for demanding creative and technical workloads.",
                "price": "2499.00",
                "category": "Laptops",
                "tags": ["Apple", "Premium"]
            },
            {
                "name": "Dell XPS 14",
                "description": "Premium Dell laptop featuring a high-resolution display and modern Intel processor.",
                "price": "2299.00",
                "category": "Laptops",
                "tags": ["Dell", "Premium"]
            },
            {
                "name": "Lenovo ThinkPad E14",
                "description": "Business laptop designed for productivity, reliability and everyday office work.",
                "price": "1199.00",
                "category": "Laptops",
                "tags": ["Lenovo"]
            },
            {
                "name": "Lenovo Yoga 7",
                "description": "Convertible Lenovo laptop with touchscreen functionality and flexible design.",
                "price": "1399.00",
                "category": "Laptops",
                "tags": ["Lenovo"]
            },
            {
                "name": "iPad Air 11-inch",
                "description": "Apple tablet suitable for productivity, entertainment and creative tasks.",
                "price": "899.00",
                "category": "Tablets",
                "tags": ["Apple"]
            },
            {
                "name": "iPad Pro 13-inch",
                "description": "High-performance Apple tablet with advanced display technology.",
                "price": "1699.00",
                "category": "Tablets",
                "tags": ["Apple", "Premium"]
            },
            {
                "name": "Samsung Galaxy Tab S10+",
                "description": "Samsung premium Android tablet with a large AMOLED display.",
                "price": "1199.00",
                "category": "Tablets",
                "tags": ["Samsung", "Premium"]
            },
            {
                "name": "Samsung Galaxy Tab S10 FE",
                "description": "Versatile Samsung tablet designed for entertainment and productivity.",
                "price": "699.00",
                "category": "Tablets",
                "tags": ["Samsung"]
            },
            {
                "name": "Sony WH-1000XM6",
                "description": "Wireless noise-cancelling over-ear headphones with premium sound quality.",
                "price": "549.00",
                "category": "Audio",
                "tags": ["Sony", "Wireless", "Bluetooth", "Premium"]
            },
            {
                "name": "Samsung Galaxy Buds3 Pro",
                "description": "Samsung wireless earbuds with active noise cancellation.",
                "price": "299.00",
                "category": "Audio",
                "tags": ["Samsung", "Wireless", "Bluetooth"]
            },
            {
                "name": "Apple AirPods Pro 3",
                "description": "Apple wireless earbuds featuring active noise cancellation and spatial audio.",
                "price": "329.00",
                "category": "Audio",
                "tags": ["Apple", "Wireless", "Bluetooth"]
            },
            {
                "name": "JBL Charge 6",
                "description": "Portable Bluetooth speaker designed for indoor and outdoor entertainment.",
                "price": "229.00",
                "category": "Audio",
                "tags": ["Wireless", "Bluetooth"]
            },
            {
                "name": "Sony Alpha A7 IV",
                "description": "Full-frame mirrorless camera designed for professional photography and video.",
                "price": "2799.00",
                "category": "Cameras",
                "tags": ["Sony", "Premium"]
            },
            {
                "name": "Canon EOS R6 Mark II",
                "description": "Full-frame mirrorless camera designed for professional photography and video production.",
                "price": "2999.00",
                "category": "Cameras",
                "tags": ["Premium"]
            },
        ]

        for item in products_data:
            product, _ = Product.objects.update_or_create(
                name=item["name"],
                defaults={
                    "description": item["description"],
                    "price": item["price"],
                    "category": categories[item["category"]],
                }
            )

            product.tags.set([
                tags[tag_name] for tag_name in item["tags"]
            ])

        self.stdout.write(
            self.style.SUCCESS(
                "Electronics catalogue sample data created successfully!"
            )
        )

        self.stdout.write(f"Categories: {Category.objects.count()}")
        self.stdout.write(f"Tags: {Tag.objects.count()}")
        self.stdout.write(f"Products: {Product.objects.count()}")
