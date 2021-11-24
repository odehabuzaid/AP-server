from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import TodoUserCreationForm
from .models import TodoUser


class TodoAdmin(UserAdmin):
    add_form = TodoUserCreationForm
    model = TodoUser
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = (
        (
            None,
            {"fields": ("username", "email", "first_name", "last_name", "password")},
        ),
    )


# Register your models here.
admin.site.register(TodoUser, TodoAdmin)
