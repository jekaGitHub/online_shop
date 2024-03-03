from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, CatalogListView, CatalogDetailView, ContactTemplateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('products/', CatalogListView.as_view(), name='product_list'),
    path('contacts/', ContactTemplateView.as_view(), name='contact'),
    path('catalog/<int:pk>', CatalogDetailView.as_view(), name='product_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
