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
    price = models.DecimalField(decimal_places=2, max_digits=7, verbose_name="Цена за покупку")
    created_at = models.DateField(verbose_name="Дата создания")
    updated_at = models.DateField(verbose_name="Дата последнего изменения")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number_version = models.IntegerField(default=0, verbose_name='номер версии')
    name_version = models.CharField(max_length=150, verbose_name='название версии')
    is_active_version = models.BooleanField(default=False, verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.number_version}, {self.name_version}, {self.is_active_version}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название")
    slug = models.CharField(max_length=150, verbose_name="slug", **NULLABLE)
    description = models.TextField(verbose_name="Содержимое")
    image = models.ImageField(upload_to="photo/article", verbose_name="Превью", **NULLABLE)
    created_at = models.DateField(verbose_name="Дата создания")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    views_count = models.IntegerField(default=0, verbose_name="Просмотры")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
