from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(**NULLABLE, verbose_name="Описание")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(**NULLABLE, verbose_name="Описание")
    image = models.ImageField(upload_to="photo", verbose_name="Превью", **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="catalog", verbose_name="Категория")
    price = models.DecimalField(decimal_places="2", max_digits="7", verbose_name="Цена за покупку")
    created_at = models.DateField(verbose_name="Дата создания")
    updated_at = models.DateField(verbose_name="Дата последнего изменения")
    manufactured_at = models.DateField(default="2024-02-17", verbose_name="Дата производства продукта")

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
