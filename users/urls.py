from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

from users.views import RegisterView, verify, ResetPasswordView, UserUpdateView

from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("registration/", RegisterView.as_view(), name="register"),
    path("verify/<str:token>/", verify, name="verify"),
    path("profile/", UserUpdateView.as_view(), name="profile"),
    path("password-reset/", ResetPasswordView.as_view(), name="password_reset"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
