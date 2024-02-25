from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contact, single_product

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contact, name='contact'),
    path('catalog/<int:pk>', single_product, name='page_product')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
