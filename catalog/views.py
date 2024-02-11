from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'catalog/index.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Вы отправили новое сообщение от {name}({phone}): {message}')
    return render(request, 'catalog/contact.html')
