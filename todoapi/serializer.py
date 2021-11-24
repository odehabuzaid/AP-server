from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("id", "user","task", "label", "created_at", "status",)
        labels = {"status": "complete"}
