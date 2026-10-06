from django.core.cache import cache

from catalog.models import Product


def get_products_by_category(category_id):
    """Возвращает продукты указанной категории."""
    key = f"category_{category_id}"
    products = cache.get(key)

    if not products:
        products = Product.objects.filter(category_id=category_id)
        cache.set(key, products, 60 * 15)

    return products
