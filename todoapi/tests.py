from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Task


class TaskModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(
            username="tester", password="pass"
        )
        test_user.save()
        
        test_task = Task.objects.create(
            user=test_user, task="Title", label="Medium", status=False
        )
        test_task.save()

    def test_blog_content(self):
        task = Task.objects.get(id=1)
        self.assertEqual(str(task.user), "tester")
        self.assertEqual(task.title, "Title")
        self.assertEqual(task.label, "Medium")
        self.assertEqual(task.status, False)
