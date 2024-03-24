from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from users.forms import RegistrationForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = RegistrationForm

    def get_success_url(self):
        return reverse('users:login')
