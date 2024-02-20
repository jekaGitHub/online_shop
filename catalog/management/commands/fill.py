from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        # students_list = [
        #     {},
        #     {},
        #     {}
        # ]
        #
        # students_for_create = []
        # for student in students_list:
        #     students_for_create.append(
        #         Student(**student)
        #     )
        # Student.objects.bulk_create(students_for_create)
        @staticmethod
        def json_read_categories():

        # Здесь мы получаем данные из фикстурв с категориями

        @staticmethod
        def json_read_products():

        # Здесь мы получаем данные из фикстурв с продуктами

        def handle(self, *args, **options):

            # Удалите все продукты
            # Удалите все категории

            # Списки для хранения объектов
            product_for_create = []
            category_for_create = []

            # Обходим все значения категорий из фикстуры для получения информации об одном объекте
            for category in Command.json_read_categories():
                category_for_create.append(
                    Category(название_поля=значение_из_словаря, ..., название_поля=значение_из_словаря)
                )

            # Создаем объекты в базе с помощью метода bulk_create()
            Category.objects.bulk_create(category_for_create)

            # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
            for product in Command.json_read_products():
                product_for_create.append(
                    Product(название_поля=значение_из_словаря, ...,
                            # получаем категорию из базы данных для корректной связки объектов
                            поле_категории=Category.objects.get(pk=значение_из_словаря), ...,
                            название_поля=значение_из_словаря)
                )

            # Создаем объекты в базе с помощью метода bulk_create()
            Product.objects.bulk_create(product_for_create)
