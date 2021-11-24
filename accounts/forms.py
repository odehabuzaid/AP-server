from django.contrib.auth.forms import UserCreationForm

from .models import TodoUser


class TodoUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = TodoUser
        fields = (
           
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )
