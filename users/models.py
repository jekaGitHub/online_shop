from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class User(AbstractUser):
    username = None

    avatar = models.ImageField(upload_to="users/avatar/", verbose_name="Аватар", **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name="Номер телефона", **NULLABLE)
    country = models.CharField(max_length=35, verbose_name="Страна", **NULLABLE)

    email = models.EmailField(unique=True, verbose_name="Email")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"