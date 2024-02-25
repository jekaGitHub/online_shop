from django.shortcuts import render, get_object_or_404

from catalog.models import Product


# Create your views here.
def home(request):
    products = Product.objects.all()
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


def single_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        "object": product
    }
    return render(request, 'catalog/page_product.html', context)
