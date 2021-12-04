from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class TodoUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=20, verbose_name="Email Address")
    country = models.CharField(max_length=20, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(
        blank=True,
        choices=(
            ("Male", "male"),
            ("Female", "female"),
            ("Prefer not to say", "no_preference"),
        ),
        max_length=20,
    )


    class Meta:
        verbose_name = "TodoUser"
        verbose_name_plural = "TodoUsers"
    
    def __str__(self) -> str:
        return self.email
