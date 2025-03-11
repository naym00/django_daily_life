from django.urls import path
from task import views

urlpatterns = [
    path('task-list/<int:id>/', views.task_list, name='task-list'),
]
