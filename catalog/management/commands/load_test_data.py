from django.core.management import call_command
from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    """Загружает тестовые данные."""

    help = "Загрузка тестовых данных"

    def handle(self, *args, **options):
        """Загружает данные."""

        # Удаление данных
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Загрузка фикстур
        call_command("loaddata", "categories.json")
        call_command("loaddata", "products.json")

        self.stdout.write(self.style.SUCCESS("Данные загружены"))