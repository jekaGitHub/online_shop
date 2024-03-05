from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from pytils.translit import slugify

from catalog.models import Product, Article
from django.views.generic import View, CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView


# Create your views here.
class CatalogListView(ListView):
    model = Product


class CatalogDetailView(DetailView):
    model = Product


class ContactTemplateView(TemplateView):
    template_name = "catalog/contact.html"


class HomeListView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Product.objects.all()[:5]


class ContactView(View):
    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Вы отправили новое сообщение от {name}({phone}): {message}')
        return render(request, 'catalog/contact.html')

    def get(self, request):
        return render(request, 'catalog/contact.html')


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'description', 'created_at', 'is_published', 'views_count',)
    success_url = reverse_lazy('catalog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()

        return super().form_valid(form)


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

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:view', args=[self.kwargs.get('pk')])


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('catalog:list')