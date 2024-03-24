import secrets

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView

from config import settings
from users.forms import RegistrationForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = RegistrationForm

    def get_success_url(self):
        return reverse('users:login')

    def form_valid(self, form):
        user = form.save()
        token = secrets.token_hex(16)
        user.token = token
        user.is_active = False
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/verify/{token}/'
        message = f'Привет! Для подтверждения почты тебе необходимо перейти по ссылке: {url}'
        send_mail('Верификация почты', message, settings.EMAIL_HOST_USER, [user.email])
        return super().form_valid(form)


def verify(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))
