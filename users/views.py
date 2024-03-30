import random
import secrets

from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from config import settings
from users.forms import RegistrationForm, UserForm, ResetPasswordForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = "users/register.html"

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


class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user


class ResetPasswordView(PasswordResetView):
    form_class = ResetPasswordForm
    template_name = 'users/reset_password.html'

    def get_success_url(self):
        return reverse('users:login')

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        user = User.objects.get(email=email)

        password = ''.join([str(random.randint(0, 9)) for _ in range(8)])
        user.password = make_password(password)
        user.save()
        message = f"Ваш новый пароль: {password}"
        send_mail(
            subject="Смена пароля",
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False,
        )
        return super().form_valid(form)


def restore_password(request):
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    send_mail(
        subject='Восстановление пароля',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.POST.get('email')]
    )
    request.user.set_password(make_password(new_password))
    request.user.save()
    return redirect(reverse('catalog:home'))
