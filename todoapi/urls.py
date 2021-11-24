from django.urls import path

from .views import TasksDetail, TasksList

urlpatterns = [
    path('', TasksList.as_view(), name='tasks_list'),
    path('<int:pk>/', TasksDetail.as_view(), name='tasks_details'),
]
