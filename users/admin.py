from django.contrib import admin

from users.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "password", "country", "phone")
    list_filter = ("email", "country")
    search_fields = ("email", "phone")
