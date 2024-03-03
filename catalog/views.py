from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from catalog.models import Product, Article
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView


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
    success_url = reverse_lazy('catalog:list')


class ArticleListView(ListView):
    model = Article

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'description', 'created_at', 'is_published', 'views_count',)
    success_url = reverse_lazy('catalog:list')


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('catalog:list')