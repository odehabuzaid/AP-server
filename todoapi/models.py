from accounts import models
from django import forms
from django.contrib.auth import get_user_model
from django.db import models

LABEL_CHOICES = (
    ("NoLabel", "High"),
    ("High", "High"),
    ("Medium", "Medium"),
    ("Low", "Low"),
    ("OnHold", "Hold"),
)


# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    task = models.CharField(max_length=20)
    label = models.CharField(max_length=10, choices=LABEL_CHOICES, default="NoLabel")
    du_date = forms.DateTimeField(widget=forms.TextInput(attrs={"type": "date"}))
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.task
