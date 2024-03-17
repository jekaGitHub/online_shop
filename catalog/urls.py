from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import (HomeListView, CatalogListView, CatalogDetailView, ProductCreateView, ProductUpdateView,
                           ContactTemplateView, ArticleCreateView, ArticleListView, ArticleDetailView,
                           ArticleUpdateView, ArticleDeleteView)

app_name = CatalogConfig.name

urlpatterns = [
                  path('', HomeListView.as_view(), name='home'),
                  path('products/', CatalogListView.as_view(), name='product_list'),
                  path('contacts/', ContactTemplateView.as_view(), name='contact'),
                  path('product/create/', ProductCreateView.as_view(), name='product_create'),
                  path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
                  path('catalog/<int:pk>/', CatalogDetailView.as_view(), name='product_detail'),
                  path('article/create/', ArticleCreateView.as_view(), name='create'),
                  path('articles/', ArticleListView.as_view(), name='list'),
                  path('article/view/<int:pk>/', ArticleDetailView.as_view(), name='view'),
                  path('article/edit/<int:pk>/', ArticleUpdateView.as_view(), name='edit'),
                  path('article/delete/<int:pk>/', ArticleDeleteView.as_view(), name='delete'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
