from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from catalog.models import Product, Article
from django.views.generic import CreateView, ListView, DetailView, TemplateView


# Create your views here.
class CatalogListView(ListView):
    model = Product


class CatalogDetailView(DetailView):
    model = Product


class ContactTemplateView(TemplateView):
    template_name = "catalog/contact.html"


def home(request):
    products = Product.objects.all()[:5]
    сontext = {
        "object_list": products
    }
    return render(request, 'catalog/index.html', сontext)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Вы отправили новое сообщение от {name}({phone}): {message}')
    return render(request, 'catalog/contact.html')


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'description', 'created_at', 'is_published', 'views_count',)
    success_url = reverse_lazy('catalog:index')


class ArticleListView(ListView):
    model = Article
