from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email="jeka-luda@yandex.ru",
            is_staff=True,
            is_superuser=True,
        )
        user.set_password("123zxc")
        user.save()
