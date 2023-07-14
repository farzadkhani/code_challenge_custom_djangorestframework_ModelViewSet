from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from main_app.mixins import ModelAdminMixin

from .forms import CustomUserChangeForm, CustomUserCreationForm

# Register your models here.


class UserAdmin(UserAdmin, ModelAdminMixin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = (
        "id",
        "cell_phone",
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "is_superuser",
        "last_login",
        "is_removed",
        "created_at",
        "updated_at",
    )
    list_filter = ("is_active", "is_staff", "is_superuser", "is_removed")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "password",
                    "cell_phone",
                    "email",
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "cell_phone",
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = ("email", "cell_phone", "first_name", "last_name")
    ordering = ("-id",)


admin.site.register(User, UserAdmin)
