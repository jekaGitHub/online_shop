import json

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        # Здесь мы получаем данные из фикстуры с категориями
        categories = []

        with open("../catalog_data.json", 'r') as f:
            data = json.load(f)

        for item in data:
            if item['model'] == 'catalog.category':
                categories.append(item)

        return categories

    @staticmethod
    def json_read_products():
        # Здесь мы получаем данные из фикстуры с продуктами
        products = []

        with open("../catalog_data.json", 'r') as f:
            data = json.load(f)

        for item in data:
            if item['model'] == 'catalog.product':
                products.append(item)

        return products

    def handle(self, *args, **options):

        # Удалите все продукты
        Product.objects.all().delete()
        # Удалите все категории
        Category.objects.all().delete()

        # Списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фикстуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(**category)
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фикстуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(
                Product(**product)
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
