from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
