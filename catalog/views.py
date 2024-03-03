from django.shortcuts import render, get_object_or_404

from catalog.models import Product
from django.views.generic import ListView, DetailView, TemplateView


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
