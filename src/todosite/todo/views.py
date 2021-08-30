from django.shortcuts import render
from .models import CategoryTask, Task


def task_list(request):
    """Функция отображения задач на домошней странице сайта."""
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks, 'title': 'Список дел'})


def category_list(request):
    """Функция отображения категорий задач на домошней странице сайта."""
    categories = CategoryTask.objects.all()
    return render(request, 'category_list.html', {'categories': categories})
